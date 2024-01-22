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

`SendRequest(requestType, requestId, requestData)`
Sends a single request

| Parameter | Data type | Default value | Description | Optional |
| -- | -- | -- | -- | -- |
| `requestType` | [RequestType][2] | | The type of the request | |
| `requestId` | string | \<uuid4> | A custom ID used to track the request | :white_check_mark: |
| `requestData` | dict | None | Any input the request requires | :white_check_mark: |

`SendRequestBatch(data, executionType, haltOnFailure)`
Sends one or more requests together

| Parameter | Data type | Default value | Description | Optional |
| -- | -- | -- | -- | -- |
| `data` | list[dict[str, Any]] | | A list of payloads taking the form of `SendRequest`'s parameters | |
| `executionType` | [RequestBatchExecutionType][3] | SERIAL_REALTIME | The request execution type | :white_check_mark: |
| `haltOnFailure` | bool | False | Stops the batch if one request fails | :white_check_mark: |

The `RequestType` and `RequestBatchExecutionType` enums are promoted by the extension and can be easily accessed on the component with `op.OBSWebSocket.[EnumName]`. See the [source](scripts/OBSEnums.py) for all enums and values.

Each request type's input for `requestData` can be found in the [obs-websocket documentation][1].

For batch requests, it's recommended to provide a custom `requestId` with each request. This will help you identify responses in the results table (found at OBSWebSocket/out1) where each one is logged until the next request is sent.

## Contributing

A custom Release component can be found in the project that automates the packaging, so simply make changes, increase the Version parameter (following [semver](https://semver.org)), and click the Package button.

[1]: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#general-requests
[2]: scripts/OBSEnums.py#L96
[3]: scripts/OBSEnums.py#L32