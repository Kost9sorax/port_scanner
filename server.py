import logging
from aiohttp import web
import config
from scanner import scan_port, IncorrectIpError

log = logging.getLogger('')


async def scanner(request):
    ip = request.match_info.get('ip')
    start_port = int(request.match_info.get('begin_port'))
    finish_port = int(request.match_info.get('end_port'))
    result = []
    log.info(f'scan port for {ip} from {start_port} to {finish_port}')
    if start_port > finish_port:
        log.info('The start port is larger than the end port')
        return web.Response(body='The start port is larger than the end port', status=400)
    try:
        for i in range(start_port, finish_port):
            if scan_port(ip, i):
                result.append({"port": i, "state": "open"})
            else:
                result.append({"port": i, "state": "close"})
    except IncorrectIpError:
        return web.Response(status=400, body='Incorrect ip')

    return web.json_response(result)


async def init():
    app = web.Application()
    app.router.add_get("/scan/{ip}/{begin_port}/{end_port}", scanner)
    return app


if __name__ == "__main__":
    application = init()
    web.run_app(application, host=config.HOST, port=config.PORT)
