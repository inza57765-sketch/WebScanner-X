def headers_func(result):

    print("\n\tla page est accessible....\n")

    print(result["url"])
    print(f"   Status                  : {result['status_code']}")
    print(f"   Server                  : {result['server']}")
    print(f"   Content-Type            : {result['content_type']}")
    print(f"   Cache-Control           : {result['cache_control']}")
    print(f"   X-Powered-By            : {result['x_powered_by']}")
    print(f"   X-Frame-Options         : {result['x_frame_options']}")
    print(f"   X-XSS-Protection        : {result['x_xss_protection']}")
    print(f"   Content-Security-Policy : {result['content_security_policy']}")
    print("\n")
