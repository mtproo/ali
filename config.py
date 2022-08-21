PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "32b920dffb51643028e2f6b878d4eac1"
}

MODES = {
    # Classic mode, easy to detect
    "classic": True,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": True,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True,
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www.we-have.english"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "d1cd833e886347155cc292f899891ef7"

