import { handleUpload } from "@vercel/blob/client";

export default async function handler(req, res) {
    if (req.method !== "POST") {
        return res.status(405).json({
            error: "Method not allowed"
        });
    }

    try {
        const body = req.body;

        const jsonResponse = await handleUpload({
            token: process.env.Private_BLOB_READ_WRITE_TOKEN,
            body,
            request: req,

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

        return res.status(200).json(jsonResponse);

    } catch (error) {
        console.error("Blob upload error:", error);

        return res.status(400).json({
            error: error instanceof Error
                ? error.message
                : String(error)
        });
    }
}