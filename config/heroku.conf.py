import os

bind_address = ('0.0.0.0', int(os.environ.get("PORT", 5000)))
ignore_headers = """
X-Varnish
X-Forwarded-For
X-Heroku-Dynos-In-Use
X-Request-Start
X-Heroku-Queue-Wait-Time
X-Heroku-Queue-Depth
X-Real-Ip
X-Forwarded-Proto
X-Via
X-Forwarded-Port
""".split("\n")[1:-1]
storage_backend = 'requestbin.storage.memory.MemoryStorage'
#redis_init = {
#    'host': '50.19.218.147', 'port': 10043, 'db': 0,
#    'password': os.environ.get("REDIS_PASSWORD")}

service = "requestbin.service.RequestBin"
