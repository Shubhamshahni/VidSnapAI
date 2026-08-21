import { handleUpload } from "@vercel/blob/client";

export default async function handler(request) {
    if (request.method !== "POST") {
        return new Response(
            JSON.stringify({ error: "Method not allowed" }),
            {
                status: 405,
                headers: {
                    "Content-Type": "application/json"
                }
            }
        );
    }

    try {
        const body = await request.json();
        const jsonResponse = await handleUpload({
            token: process.env.Private_BLOB_READ_WRITE_TOKEN,
            body,
            request,

            onBeforeGenerateToken: async (
                pathname,
                clientPayload,
                multipart
            ) => {
                return {
                    allowedContentTypes: [
                        "image/jpeg",
                        "image/png",
                        "image/webp"
                    ],
                    maximumSizeInBytes: 20 * 1024 * 1024,
                    addRandomSuffix: true
                };
            },

            onUploadCompleted: async ({ blob, tokenPayload }) => {
                console.log(
                    "Blob upload completed:",
                    blob.pathname
                );
            }
        });

        return Response.json(jsonResponse);

    } catch (error) {
        console.error("Blob upload error:", error);

        return Response.json(
            {
                error: error instanceof Error
                    ? error.message
                    : String(error)
            },
            { status: 400 }
        );
    }
}