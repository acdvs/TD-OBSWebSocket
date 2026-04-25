# TD-OBSWebSocket

A packaged TouchDesigner component that connects to an [obs-websocket][obs-websocket] server and receives all available events.

## Basic Usage

1. Download the .tox file from the [Releases][releases] page and place it in a location convenient for your project.
2. Drag and drop it into your project.
3. Set the Address and Port of the server in the Connection parameters tab. Set the Password if there is one.
4. If Auto-Reconnect is enabled, the component will connect to the server automatically.  
   If Auto-Reconnect is disabled, enable the Active switch to connect to the server.

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

All methods and enums mentioned below are promoted via `op.OBSWebSocket`. Each request type's necessary data can be found in the obs-websocket [documentation][requests]. All enum values can be found in the [source][obs-enums].

#### Request

Sending a request to OBS starts with creating a `Request` object.

| Parameter | Type  | Description | Default | Required |
| -- | -- | -- | -- | -- |
| 1 | [RequestType][request-type] | Request type | | ✅ |
| data | dict | Any necessary data for the request type. | None | |
| id | str | A unique ID. Directly sent back in the response. | _uuid4()_ | |

#### SendRequest

Pass an individual request to `SendRequest`.

```py
OBSWS = op.OBSWebSocket

basic_req = OBSWS.Request(OBSWS.RequestType.GET_STATS)
success = BSWS.SendRequest(basic_req)

advanced_req = OBSWS.Request(
   OBSWS.RequestType.SET_CURRENT_PROGRAM_SCENE,
   data={"sceneName": "Some Existing Scene"},
   id="unique-id",
)
success = OBSWS.SendRequest(advanced_req)
```

#### SendBatchRequest

Sending multiple requests is as easy as creating them and passing them to `SendBatchRequest` as a list.

| Parameter | Type  | Description | Default | Required |
| -- | -- | -- | -- | -- |
| 1 | list[Request] | A list of requests. | | ✅ |
| execution_type | [RequestBatchExecutionType][batch-type] | Changes how the requests are processed. | SERIAL_REALTIME | |
| halt_on_failure | bool | Stops processing requests on failure. | False | |
| id | str | A unique ID. Directly sent back in the response. Separate from individual request IDs. | _uuid4()_ | |

```py
OBSWS = op.OBSWebSocket

req1 = OBSWS.Request(OBSWS.RequestType.GET_VERSION)
req2 = OBSWS.Request(OBSWS.RequestType.GET_STATS)

success = OBSWS.SendBatchRequest([req1, req2])
success = OBSWS.SendBatchRequest(
   [req1, req2],
   execution_type=OBSWS.RequestBatchExecutionType.PARALLEL,
   halt_on_failure=True,
   id="unique-id",
)
```

## Contributing

If you are considering adding a new feature or change to the project, first create a feature request issue to document it and get feedback before proceeding. If you are considering fixing a bug, first open a bug report issue or search for an existing one.

[batch-type]: src/obs_enums.py#115
[obs-enums]: src/obs_enums.py
[obs-websocket]: https://github.com/obsproject/obs-websocket
[releases]: https://github.com/acdvs/TD-OBSWebSocket/releases
[request-type]: src/obs_enums.py#612
[requests]: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#general-requests