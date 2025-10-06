import os
import asyncio
from api_solver import create_app
import hypercorn.asyncio

async def run_server():
    # Get port from Koyeb's environment variable
    port = int(os.getenv('PORT', 8000))
    
    # Create the app
    app = create_app(
        debug=False,
        headless=True,  # Must run headless on Koyeb
        useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        browser_type="chromium",
        thread=1
    )
    
    # Configure Hypercorn to bind to 0.0.0.0 and Koyeb's PORT
    config = hypercorn.Config()
    config.bind = [f"0.0.0.0:{port}"]
    
    print(f"Starting API server on 0.0.0.0:{port}")
    await hypercorn.asyncio.serve(app, config)

if __name__ == "__main__":
    asyncio.run(run_server()) 
