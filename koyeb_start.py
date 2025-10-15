import os
import asyncio
from api_solver import create_app
import hypercorn.asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

async def run_server():
    # Get port from Koyeb's environment variable
    port = int(os.getenv('PORT', 8000))
    
    # Parse proxy from environment variable
    proxy_url = os.getenv('PROXY_URL')
    proxy_dict = None
    
    if proxy_url:
        try:
            # Parse format: IP:PORT:USERNAME:PASSWORD
            parts = proxy_url.split(':')
            if len(parts) == 4:
                ip, port_proxy, username, password = parts
                # Format as http proxy with authentication
                proxy_dict = {
                    'server': f'http://{ip}:{port_proxy}',
                    'username': username,
                    'password': password
                }
                print(f"Proxy configured: {ip}:{port_proxy}")
            elif len(parts) == 2:
                # Format without authentication: IP:PORT
                ip, port_proxy = parts
                proxy_dict = {
                    'server': f'http://{ip}:{port_proxy}'
                }
                print(f"Proxy configured (no auth): {ip}:{port_proxy}")
        except Exception as e:
            print(f"Error parsing proxy URL: {e}")
    
    # Create the app with all required parameters
    app = create_app(
        debug=False,
        headless=True,  # Must run headless on Koyeb
        useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        browser_type="chromium",
        thread=1,
        proxy_support=bool(proxy_dict),  # Enable if proxy is configured
        proxy=proxy_dict  # Pass the proxy configuration
    )
    
    # Configure Hypercorn to bind to 0.0.0.0 and Koyeb's PORT
    config = hypercorn.Config()
    config.bind = [f"0.0.0.0:{port}"]
    
    print(f"Starting API server on 0.0.0.0:{port}")
    await hypercorn.asyncio.serve(app, config)

if __name__ == "__main__":
    asyncio.run(run_server())
