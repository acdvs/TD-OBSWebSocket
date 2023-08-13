# TD-OBSWebSocket

A packaged TouchDesigner component that connects to an [OBS](https://obsproject.com) WebSocket server and receives all available events.

## Basic Usage

1. Download the .tox file from the `/dist` folder and place it in a location convenient for your project.
2. Drag and drop it into your project.
3. Set the Address and Port of the server in the Connection parameters tab. Set the Password if there is one.
4. If Auto-Reconnect is enabled: the component will connect to the server automatically.  
   If Auto-Reconnect is disabled: enable the Active switch to connect to the server.

Once connected, any event data received will be set in the corresponding parameter. This makes the data easy to consume by, for example, connecting a Parameter Execute DAT to the OBSWebSocket component.

## Features

### High-Volume Events

Several events are considered "high-volume" and must be individually opted into to receive them. You can do this in the Connection parameters tab. These events are:

- Input Volume Meters
- Input Active State Changed
- Input Show State Changed
- Scene Item Transform Changed

It's possible to enable or disable high-volume events while connected to the server, though doing so will force a reconnect.

### Sending Requests

Two methods on the OBSWebSocket component can be used to send requests to OBS.

- `SendRequest(requestType, requestId, requestData)` - Sends a single request

  - `requestType` - A [`RequestType`](scripts/OBSEnums.py#L96)
  - `requestId` - A custom ID string used to track the request (default = uuid4)
  - `requestData` - A dict containing any input the request requires (default = `None`)

- `SendRequestBatch(data, executionType, haltOnFailure)` - Sends one or more requests together

  - `data` - An array of dicts with the form:

    ```python
    {
        "requestType": RequestType,
        # A custom ID string used to track the request (optional)
        "requestId": str,
        # A dict containing any input the request requires (optional)
        "requestData": dict
    }
    ```

  - `executionType` - A [`RequestBatchExecutionType`](scripts/OBSEnums.py#L32) (default = `SERIAL_REALTIME`)
  - `haltOnFailure` - Stops the batch if one request fails (default = `False`)

The `RequestType` and `RequestBatchExecutionType` enums are promoted by the extension and can be easily accessed on the component with `op.OBSWebSocket.[EnumName]`. See the [source](scripts/OBSEnums.py) for all enums and values.

Each request type's input for `requestData` can be found in the [obs-websocket documentation][1].

For batch requests, it's recommended to provide a custom `requestId` with each request. This will help you identify responses in the results table (found at OBSWebSocket/out1) where each one is logged until the next request is sent.

## Contributing

A custom Release component can be found in the project that automates the packaging, so simply make changes, increase the Version parameter (following [semver](https://semver.org)), and click the Package button.

[1]: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#general-requests