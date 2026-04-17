websocketOP = op("websocket").asType(websocketDAT)


def onValueChange(channel, sampleIndex, val, prev):
    if (
        not parent().par.Connected
        and parent().par.Autoreconnect
        and parent().par.Address != ""
        and parent().par.Port != ""
    ):
        websocketOP.par.reset.pulse()
