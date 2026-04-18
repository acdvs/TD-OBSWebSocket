def onValueChange(channel, sample_index, val, prev):
    if (
        not parent().par.Connected
        and parent().par.Autoreconnect
        and parent().par.Address != ""
        and parent().par.Port != ""
    ):
        websocket_op = op("websocket").asType(websocketDAT)
        websocket_op.par.reset.pulse()
