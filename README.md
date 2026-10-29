# Affiliate Website Generator V9.2

V9.2 keeps the V9 reference-template architecture and adds **DeepSeek API support**.

## AI providers
- **Auto**: tries OpenAI first, then DeepSeek if OpenAI is unavailable/fails.
- **OpenAI**: uses the OpenAI Responses API + web search.
- **DeepSeek**: uses the OpenAI-compatible DeepSeek Chat Completions API.

Keys can be entered in the UI or supplied with environment variables:
- `OPENAI_API_KEY`
- `DEEPSEEK_API_KEY`
- `SERPAPI_KEY`
- Optional `DEEPSEEK_BASE_URL` (defaults to `https://api.deepseek.com`)
- Optional `DEEPSEEK_MODEL` (defaults to `deepseek-chat`)

The selected V9 design shell remains the source of the generated site's visual structure. Product-specific content, metadata, links and local images are rebuilt for the requested product.

Before publishing, verify product claims, pricing, guarantees, testimonials, certifications and image usage rights.

See [IMAGE_NAMING_GUIDE.md](IMAGE_NAMING_GUIDE.md) for the filenames to use when uploading your own product images.
