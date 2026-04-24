from enum import unique, IntEnum, Enum

@unique
class EventSubscription(IntEnum):
    NONE = 0
    '''
    Subcription value used to disable all events.
    
    Initial version: 5.0.0
    '''
    GENERAL = 1 << 0
    '''
    Subscription value to receive events in the `General` category.
    
    Initial version: 5.0.0
    '''
    CONFIG = 1 << 1
    '''
    Subscription value to receive events in the `Config` category.
    
    Initial version: 5.0.0
    '''
    SCENES = 1 << 2
    '''
    Subscription value to receive events in the `Scenes` category.
    
    Initial version: 5.0.0
    '''
    INPUTS = 1 << 3
    '''
    Subscription value to receive events in the `Inputs` category.
    
    Initial version: 5.0.0
    '''
    TRANSITIONS = 1 << 4
    '''
    Subscription value to receive events in the `Transitions` category.
    
    Initial version: 5.0.0
    '''
    FILTERS = 1 << 5
    '''
    Subscription value to receive events in the `Filters` category.
    
    Initial version: 5.0.0
    '''
    OUTPUTS = 1 << 6
    '''
    Subscription value to receive events in the `Outputs` category.
    
    Initial version: 5.0.0
    '''
    SCENE_ITEMS = 1 << 7
    '''
    Subscription value to receive events in the `SceneItems` category.
    
    Initial version: 5.0.0
    '''
    MEDIA_INPUTS = 1 << 8
    '''
    Subscription value to receive events in the `MediaInputs` category.
    
    Initial version: 5.0.0
    '''
    VENDORS = 1 << 9
    '''
    Subscription value to receive the `VendorEvent` event.
    
    Initial version: 5.0.0
    '''
    UI = 1 << 10
    '''
    Subscription value to receive events in the `Ui` category.
    
    Initial version: 5.0.0
    '''
    CANVASES = 1 << 11
    '''
    Subscription value to receive events in the `Canvases` category.
    
    Initial version: 5.7.0
    '''
    ALL = GENERAL | CONFIG | SCENES | INPUTS | TRANSITIONS | FILTERS | OUTPUTS | SCENE_ITEMS | MEDIA_INPUTS | VENDORS | UI | CANVASES
    '''
    Helper to receive all non-high-volume events.
    
    Initial version: 5.0.0
    '''
    INPUT_VOLUME_METERS = 1 << 16
    '''
    Subscription value to receive the `InputVolumeMeters` high-volume event.
    
    Initial version: 5.0.0
    '''
    INPUT_ACTIVE_STATE_CHANGED = 1 << 17
    '''
    Subscription value to receive the `InputActiveStateChanged` high-volume event.
    
    Initial version: 5.0.0
    '''
    INPUT_SHOW_STATE_CHANGED = 1 << 18
    '''
    Subscription value to receive the `InputShowStateChanged` high-volume event.
    
    Initial version: 5.0.0
    '''
    SCENE_ITEM_TRANSFORM_CHANGED = 1 << 19
    '''
    Subscription value to receive the `SceneItemTransformChanged` high-volume event.
    
    Initial version: 5.0.0
    '''

@unique
class RequestBatchExecutionType(Enum):
    NONE = -1
    '''
    Not a request batch.
    
    Initial version: 5.0.0
    '''
    SERIAL_REALTIME = 0
    '''
    A request batch which processes all requests serially, as fast as possible.
    
    Note: To introduce artificial delay, use the `Sleep` request and the `sleepMillis` request field.
    
    Initial version: 5.0.0
    '''
    SERIAL_FRAME = 1
    '''
    A request batch type which processes all requests serially, in sync with the graphics thread. Designed to provide high accuracy for animations.
    
    Note: To introduce artificial delay, use the `Sleep` request and the `sleepFrames` request field.
    
    Initial version: 5.0.0
    '''
    PARALLEL = 2
    '''
    A request batch type which processes all requests using all available threads in the thread pool.
    
    Note: This is mainly experimental, and only really shows its colors during requests which require lots of
    active processing, like `GetSourceScreenshot`.
    
    Initial version: 5.0.0
    '''

@unique
class RequestStatus(IntEnum):
    UNKNOWN = 0
    '''
    Unknown status, should never be used.
    
    Initial version: 5.0.0
    '''
    NO_ERROR = 10
    '''
    For internal use to signify a successful field check.
    
    Initial version: 5.0.0
    '''
    SUCCESS = 100
    '''
    The request has succeeded.
    
    Initial version: 5.0.0
    '''
    MISSING_REQUEST_TYPE = 203
    '''
    The `requestType` field is missing from the request data.
    
    Initial version: 5.0.0
    '''
    UNKNOWN_REQUEST_TYPE = 204
    '''
    The request type is invalid or does not exist.
    
    Initial version: 5.0.0
    '''
    GENERIC_ERROR = 205
    '''
    Generic error code.
    
    Note: A comment is required to be provided by obs-websocket.
    
    Initial version: 5.0.0
    '''
    UNSUPPORTED_REQUEST_BATCH_EXECUTION_TYPE = 206
    '''
    The request batch execution type is not supported.
    
    Initial version: 5.0.0
    '''
    NOT_READY = 207
    '''
    The server is not ready to handle the request.
    
    Note: This usually occurs during OBS scene collection change or exit. Requests may be tried again after a delay if this code is given.
    
    Initial version: 5.3.0
    '''
    MISSING_REQUEST_FIELD = 300
    '''
    A required request field is missing.
    
    Initial version: 5.0.0
    '''
    MISSING_REQUEST_DATA = 301
    '''
    The request does not have a valid requestData object.
    
    Initial version: 5.0.0
    '''
    INVALID_REQUEST_FIELD = 400
    '''
    Generic invalid request field message.
    
    Note: A comment is required to be provided by obs-websocket.
    
    Initial version: 5.0.0
    '''
    INVALID_REQUEST_FIELD_TYPE = 401
    '''
    A request field has the wrong data type.
    
    Initial version: 5.0.0
    '''
    REQUEST_FIELD_OUT_OF_RANGE = 402
    '''
    A request field (number) is outside of the allowed range.
    
    Initial version: 5.0.0
    '''
    REQUEST_FIELD_EMPTY = 403
    '''
    A request field (string or array) is empty and cannot be.
    
    Initial version: 5.0.0
    '''
    TOO_MANY_REQUEST_FIELDS = 404
    '''
    There are too many request fields (eg. a request takes two optionals, where only one is allowed at a time).
    
    Initial version: 5.0.0
    '''
    OUTPUT_RUNNING = 500
    '''
    An output is running and cannot be in order to perform the request.
    
    Initial version: 5.0.0
    '''
    OUTPUT_NOT_RUNNING = 501
    '''
    An output is not running and should be.
    
    Initial version: 5.0.0
    '''
    OUTPUT_PAUSED = 502
    '''
    An output is paused and should not be.
    
    Initial version: 5.0.0
    '''
    OUTPUT_NOT_PAUSED = 503
    '''
    An output is not paused and should be.
    
    Initial version: 5.0.0
    '''
    OUTPUT_DISABLED = 504
    '''
    An output is disabled and should not be.
    
    Initial version: 5.0.0
    '''
    STUDIO_MODE_ACTIVE = 505
    '''
    Studio mode is active and cannot be.
    
    Initial version: 5.0.0
    '''
    STUDIO_MODE_NOT_ACTIVE = 506
    '''
    Studio mode is not active and should be.
    
    Initial version: 5.0.0
    '''
    RESOURCE_NOT_FOUND = 600
    '''
    The resource was not found.
    
    Note: Resources are any kind of object in obs-websocket, like inputs, profiles, outputs, etc.
    
    Initial version: 5.0.0
    '''
    RESOURCE_ALREADY_EXISTS = 601
    '''
    The resource already exists.
    
    Initial version: 5.0.0
    '''
    INVALID_RESOURCE_TYPE = 602
    '''
    The type of resource found is invalid.
    
    Initial version: 5.0.0
    '''
    NOT_ENOUGH_RESOURCES = 603
    '''
    There are not enough instances of the resource in order to perform the request.
    
    Initial version: 5.0.0
    '''
    INVALID_RESOURCE_STATE = 604
    '''
    The state of the resource is invalid. For example, if the resource is blocked from being accessed.
    
    Initial version: 5.0.0
    '''
    INVALID_INPUT_KIND = 605
    '''
    The specified input (obs_source_t-OBS_SOURCE_TYPE_INPUT) had the wrong kind.
    
    Initial version: 5.0.0
    '''
    RESOURCE_NOT_CONFIGURABLE = 606
    '''
    The resource does not support being configured.
    
    This is particularly relevant to transitions, where they do not always have changeable settings.
    
    Initial version: 5.0.0
    '''
    INVALID_FILTER_KIND = 607
    '''
    The specified filter (obs_source_t-OBS_SOURCE_TYPE_FILTER) had the wrong kind.
    
    Initial version: 5.0.0
    '''
    RESOURCE_CREATION_FAILED = 700
    '''
    Creating the resource failed.
    
    Initial version: 5.0.0
    '''
    RESOURCE_ACTION_FAILED = 701
    '''
    Performing an action on the resource failed.
    
    Initial version: 5.0.0
    '''
    REQUEST_PROCESSING_FAILED = 702
    '''
    Processing the request failed unexpectedly.
    
    Note: A comment is required to be provided by obs-websocket.
    
    Initial version: 5.0.0
    '''
    CANNOT_ACT = 703
    '''
    The combination of request fields cannot be used to perform an action.
    
    Initial version: 5.0.0
    '''

@unique
class ObsOutputState(Enum):
    OBS_WEBSOCKET_OUTPUT_UNKNOWN = 'OBS_WEBSOCKET_OUTPUT_UNKNOWN'
    '''
    Unknown state.
    
    Initial version: 5.0.0
    '''
    OBS_WEBSOCKET_OUTPUT_STARTING = 'OBS_WEBSOCKET_OUTPUT_STARTING'
    '''
    The output is starting.
    
    Initial version: 5.0.0
    '''
    OBS_WEBSOCKET_OUTPUT_STARTED = 'OBS_WEBSOCKET_OUTPUT_STARTED'
    '''
    The input has started.
    
    Initial version: 5.0.0
    '''
    OBS_WEBSOCKET_OUTPUT_STOPPING = 'OBS_WEBSOCKET_OUTPUT_STOPPING'
    '''
    The output is stopping.
    
    Initial version: 5.0.0
    '''
    OBS_WEBSOCKET_OUTPUT_STOPPED = 'OBS_WEBSOCKET_OUTPUT_STOPPED'
    '''
    The output has stopped.
    
    Initial version: 5.0.0
    '''
    OBS_WEBSOCKET_OUTPUT_RECONNECTING = 'OBS_WEBSOCKET_OUTPUT_RECONNECTING'
    '''
    The output has disconnected and is reconnecting.
    
    Initial version: 5.0.0
    '''
    OBS_WEBSOCKET_OUTPUT_RECONNECTED = 'OBS_WEBSOCKET_OUTPUT_RECONNECTED'
    '''
    The output has reconnected successfully.
    
    Initial version: 5.1.0
    '''
    OBS_WEBSOCKET_OUTPUT_PAUSED = 'OBS_WEBSOCKET_OUTPUT_PAUSED'
    '''
    The output is now paused.
    
    Initial version: 5.1.0
    '''
    OBS_WEBSOCKET_OUTPUT_RESUMED = 'OBS_WEBSOCKET_OUTPUT_RESUMED'
    '''
    The output has been resumed (unpaused).
    
    Initial version: 5.0.0
    '''

@unique
class ObsMediaInputAction(Enum):
    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NONE = 'OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NONE'
    '''
    No action.
    
    Initial version: 5.0.0
    '''
    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PLAY = 'OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PLAY'
    '''
    Play the media input.
    
    Initial version: 5.0.0
    '''
    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PAUSE = 'OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PAUSE'
    '''
    Pause the media input.
    
    Initial version: 5.0.0
    '''
    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_STOP = 'OBS_WEBSOCKET_MEDIA_INPUT_ACTION_STOP'
    '''
    Stop the media input.
    
    Initial version: 5.0.0
    '''
    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART = 'OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART'
    '''
    Restart the media input.
    
    Initial version: 5.0.0
    '''
    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NEXT = 'OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NEXT'
    '''
    Go to the next playlist item.
    
    Initial version: 5.0.0
    '''
    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PREVIOUS = 'OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PREVIOUS'
    '''
    Go to the previous playlist item.
    
    Initial version: 5.0.0
    '''

@unique
class WebSocketCloseCode(IntEnum):
    DONT_CLOSE = 0
    '''
    For internal use only to tell the request handler not to perform any close action.
    
    Initial version: 5.0.0
    '''
    UNKNOWN_REASON = 4000
    '''
    Unknown reason, should never be used.
    
    Initial version: 5.0.0
    '''
    MESSAGE_DECODE_ERROR = 4002
    '''
    The server was unable to decode the incoming websocket message.
    
    Initial version: 5.0.0
    '''
    MISSING_DATA_FIELD = 4003
    '''
    A data field is required but missing from the payload.
    
    Initial version: 5.0.0
    '''
    INVALID_DATA_FIELD_TYPE = 4004
    '''
    A data field's value type is invalid.
    
    Initial version: 5.0.0
    '''
    INVALID_DATA_FIELD_VALUE = 4005
    '''
    A data field's value is invalid.
    
    Initial version: 5.0.0
    '''
    UNKNOWN_OP_CODE = 4006
    '''
    The specified `op` was invalid or missing.
    
    Initial version: 5.0.0
    '''
    NOT_IDENTIFIED = 4007
    '''
    The client sent a websocket message without first sending `Identify` message.
    
    Initial version: 5.0.0
    '''
    ALREADY_IDENTIFIED = 4008
    '''
    The client sent an `Identify` message while already identified.
    
    Note: Once a client has identified, only `Reidentify` may be used to change session parameters.
    
    Initial version: 5.0.0
    '''
    AUTHENTICATION_FAILED = 4009
    '''
    The authentication attempt (via `Identify`) failed.
    
    Initial version: 5.0.0
    '''
    UNSUPPORTED_RPC_VERSION = 4010
    '''
    The server detected the usage of an old version of the obs-websocket RPC protocol.
    
    Initial version: 5.0.0
    '''
    SESSION_INVALIDATED = 4011
    '''
    The websocket session has been invalidated by the obs-websocket server.
    
    Note: This is the code used by the `Kick` button in the UI Session List. If you receive this code, you must not automatically reconnect.
    
    Initial version: 5.0.0
    '''
    UNSUPPORTED_FEATURE = 4012
    '''
    A requested feature is not supported due to hardware/software limitations.
    
    Initial version: 5.0.0
    '''

@unique
class WebSocketOpCode(IntEnum):
    HELLO = 0
    '''
    The initial message sent by obs-websocket to newly connected clients.
    
    Initial version: 5.0.0
    '''
    IDENTIFY = 1
    '''
    The message sent by a newly connected client to obs-websocket in response to a `Hello`.
    
    Initial version: 5.0.0
    '''
    IDENTIFIED = 2
    '''
    The response sent by obs-websocket to a client after it has successfully identified with obs-websocket.
    
    Initial version: 5.0.0
    '''
    REIDENTIFY = 3
    '''
    The message sent by an already-identified client to update identification parameters.
    
    Initial version: 5.0.0
    '''
    EVENT = 5
    '''
    The message sent by obs-websocket containing an event payload.
    
    Initial version: 5.0.0
    '''
    REQUEST = 6
    '''
    The message sent by a client to obs-websocket to perform a request.
    
    Initial version: 5.0.0
    '''
    REQUEST_RESPONSE = 7
    '''
    The message sent by obs-websocket in response to a particular request from a client.
    
    Initial version: 5.0.0
    '''
    REQUEST_BATCH = 8
    '''
    The message sent by a client to obs-websocket to perform a batch of requests.
    
    Initial version: 5.0.0
    '''
    REQUEST_BATCH_RESPONSE = 9
    '''
    The message sent by obs-websocket in response to a particular batch of requests from a client.
    
    Initial version: 5.0.0
    '''

@unique
class RequestType(Enum):
    GET_CANVAS_LIST = 'GetCanvasList'
    '''
    Gets an array of canvases in OBS.
    
    Initial version: 5.7.0
    '''
    GET_PERSISTENT_DATA = 'GetPersistentData'
    '''
    Gets the value of a "slot" from the selected persistent data realm.
    
    Initial version: 5.0.0
    '''
    SET_PERSISTENT_DATA = 'SetPersistentData'
    '''
    Sets the value of a "slot" from the selected persistent data realm.
    
    Initial version: 5.0.0
    '''
    GET_SCENE_COLLECTION_LIST = 'GetSceneCollectionList'
    '''
    Gets an array of all scene collections
    
    Initial version: 5.0.0
    '''
    SET_CURRENT_SCENE_COLLECTION = 'SetCurrentSceneCollection'
    '''
    Switches to a scene collection.
    
    Note: This will block until the collection has finished changing.
    
    Initial version: 5.0.0
    '''
    CREATE_SCENE_COLLECTION = 'CreateSceneCollection'
    '''
    Creates a new scene collection, switching to it in the process.
    
    Note: This will block until the collection has finished changing.
    
    Initial version: 5.0.0
    '''
    GET_PROFILE_LIST = 'GetProfileList'
    '''
    Gets an array of all profiles
    
    Initial version: 5.0.0
    '''
    SET_CURRENT_PROFILE = 'SetCurrentProfile'
    '''
    Switches to a profile.
    
    Initial version: 5.0.0
    '''
    CREATE_PROFILE = 'CreateProfile'
    '''
    Creates a new profile, switching to it in the process
    
    Initial version: 5.0.0
    '''
    REMOVE_PROFILE = 'RemoveProfile'
    '''
    Removes a profile. If the current profile is chosen, it will change to a different profile first.
    
    Initial version: 5.0.0
    '''
    GET_PROFILE_PARAMETER = 'GetProfileParameter'
    '''
    Gets a parameter from the current profile's configuration.
    
    Initial version: 5.0.0
    '''
    SET_PROFILE_PARAMETER = 'SetProfileParameter'
    '''
    Sets the value of a parameter in the current profile's configuration.
    
    Initial version: 5.0.0
    '''
    GET_VIDEO_SETTINGS = 'GetVideoSettings'
    '''
    Gets the current video settings.
    
    Note: To get the true FPS value, divide the FPS numerator by the FPS denominator. Example: `60000/1001`
    
    Initial version: 5.0.0
    '''
    SET_VIDEO_SETTINGS = 'SetVideoSettings'
    '''
    Sets the current video settings.
    
    Note: Fields must be specified in pairs. For example, you cannot set only `baseWidth` without needing to specify `baseHeight`.
    
    Initial version: 5.0.0
    '''
    GET_STREAM_SERVICE_SETTINGS = 'GetStreamServiceSettings'
    '''
    Gets the current stream service settings (stream destination).
    
    Initial version: 5.0.0
    '''
    SET_STREAM_SERVICE_SETTINGS = 'SetStreamServiceSettings'
    '''
    Sets the current stream service settings (stream destination).
    
    Note: Simple RTMP settings can be set with type `rtmp_custom` and the settings fields `server` and `key`.
    
    Initial version: 5.0.0
    '''
    GET_RECORD_DIRECTORY = 'GetRecordDirectory'
    '''
    Gets the current directory that the record output is set to.
    
    Initial version: 5.0.0
    '''
    SET_RECORD_DIRECTORY = 'SetRecordDirectory'
    '''
    Sets the current directory that the record output writes files to.
    
    Initial version: 5.3.0
    '''
    GET_SOURCE_FILTER_KIND_LIST = 'GetSourceFilterKindList'
    '''
    Gets an array of all available source filter kinds.
    
    Similar to `GetInputKindList`
    
    Initial version: 5.4.0
    '''
    GET_SOURCE_FILTER_LIST = 'GetSourceFilterList'
    '''
    Gets an array of all of a source's filters.
    
    Initial version: 5.0.0
    '''
    GET_SOURCE_FILTER_DEFAULT_SETTINGS = 'GetSourceFilterDefaultSettings'
    '''
    Gets the default settings for a filter kind.
    
    Initial version: 5.0.0
    '''
    CREATE_SOURCE_FILTER = 'CreateSourceFilter'
    '''
    Creates a new filter, adding it to the specified source.
    
    Initial version: 5.0.0
    '''
    REMOVE_SOURCE_FILTER = 'RemoveSourceFilter'
    '''
    Removes a filter from a source.
    
    Initial version: 5.0.0
    '''
    SET_SOURCE_FILTER_NAME = 'SetSourceFilterName'
    '''
    Sets the name of a source filter (rename).
    
    Initial version: 5.0.0
    '''
    GET_SOURCE_FILTER = 'GetSourceFilter'
    '''
    Gets the info for a specific source filter.
    
    Initial version: 5.0.0
    '''
    SET_SOURCE_FILTER_INDEX = 'SetSourceFilterIndex'
    '''
    Sets the index position of a filter on a source.
    
    Initial version: 5.0.0
    '''
    SET_SOURCE_FILTER_SETTINGS = 'SetSourceFilterSettings'
    '''
    Sets the settings of a source filter.
    
    Initial version: 5.0.0
    '''
    SET_SOURCE_FILTER_ENABLED = 'SetSourceFilterEnabled'
    '''
    Sets the enable state of a source filter.
    
    Initial version: 5.0.0
    '''
    GET_VERSION = 'GetVersion'
    '''
    Gets data about the current plugin and RPC version.
    
    Initial version: 5.0.0
    '''
    GET_STATS = 'GetStats'
    '''
    Gets statistics about OBS, obs-websocket, and the current session.
    
    Initial version: 5.0.0
    '''
    BROADCAST_CUSTOM_EVENT = 'BroadcastCustomEvent'
    '''
    Broadcasts a `CustomEvent` to all WebSocket clients. Receivers are clients which are identified and subscribed.
    
    Initial version: 5.0.0
    '''
    CALL_VENDOR_REQUEST = 'CallVendorRequest'
    '''
    Call a request registered to a vendor.
    
    A vendor is a unique name registered by a third-party plugin or script, which allows for custom requests and events to be added to obs-websocket.
    If a plugin or script implements vendor requests or events, documentation is expected to be provided with them.
    
    Initial version: 5.0.0
    '''
    GET_HOTKEY_LIST = 'GetHotkeyList'
    '''
    Gets an array of all hotkey names in OBS.
    
    Note: Hotkey functionality in obs-websocket comes as-is, and we do not guarantee support if things are broken. In 9/10 usages of hotkey requests, there exists a better, more reliable method via other requests.
    
    Initial version: 5.0.0
    '''
    TRIGGER_HOTKEY_BY_NAME = 'TriggerHotkeyByName'
    '''
    Triggers a hotkey using its name. See `GetHotkeyList`.
    
    Note: Hotkey functionality in obs-websocket comes as-is, and we do not guarantee support if things are broken. In 9/10 usages of hotkey requests, there exists a better, more reliable method via other requests.
    
    Initial version: 5.0.0
    '''
    TRIGGER_HOTKEY_BY_KEY_SEQUENCE = 'TriggerHotkeyByKeySequence'
    '''
    Triggers a hotkey using a sequence of keys.
    
    Note: Hotkey functionality in obs-websocket comes as-is, and we do not guarantee support if things are broken. In 9/10 usages of hotkey requests, there exists a better, more reliable method via other requests.
    
    Initial version: 5.0.0
    '''
    SLEEP = 'Sleep'
    '''
    Sleeps for a time duration or number of frames. Only available in request batches with types `SERIAL_REALTIME` or `SERIAL_FRAME`.
    
    Initial version: 5.0.0
    '''
    GET_INPUT_LIST = 'GetInputList'
    '''
    Gets an array of all inputs in OBS.
    
    Initial version: 5.0.0
    '''
    GET_INPUT_KIND_LIST = 'GetInputKindList'
    '''
    Gets an array of all available input kinds in OBS.
    
    Initial version: 5.0.0
    '''
    GET_SPECIAL_INPUTS = 'GetSpecialInputs'
    '''
    Gets the names of all special inputs.
    
    Initial version: 5.0.0
    '''
    CREATE_INPUT = 'CreateInput'
    '''
    Creates a new input, adding it as a scene item to the specified scene.
    
    Initial version: 5.0.0
    '''
    REMOVE_INPUT = 'RemoveInput'
    '''
    Removes an existing input.
    
    Note: Will immediately remove all associated scene items.
    
    Initial version: 5.0.0
    '''
    SET_INPUT_NAME = 'SetInputName'
    '''
    Sets the name of an input (rename).
    
    Initial version: 5.0.0
    '''
    GET_INPUT_DEFAULT_SETTINGS = 'GetInputDefaultSettings'
    '''
    Gets the default settings for an input kind.
    
    Initial version: 5.0.0
    '''
    GET_INPUT_SETTINGS = 'GetInputSettings'
    '''
    Gets the settings of an input.
    
    Note: Does not include defaults. To create the entire settings object, overlay `inputSettings` over the `defaultInputSettings` provided by `GetInputDefaultSettings`.
    
    Initial version: 5.0.0
    '''
    SET_INPUT_SETTINGS = 'SetInputSettings'
    '''
    Sets the settings of an input.
    
    Initial version: 5.0.0
    '''
    GET_INPUT_MUTE = 'GetInputMute'
    '''
    Gets the audio mute state of an input.
    
    Initial version: 5.0.0
    '''
    SET_INPUT_MUTE = 'SetInputMute'
    '''
    Sets the audio mute state of an input.
    
    Initial version: 5.0.0
    '''
    TOGGLE_INPUT_MUTE = 'ToggleInputMute'
    '''
    Toggles the audio mute state of an input.
    
    Initial version: 5.0.0
    '''
    GET_INPUT_VOLUME = 'GetInputVolume'
    '''
    Gets the current volume setting of an input.
    
    Initial version: 5.0.0
    '''
    SET_INPUT_VOLUME = 'SetInputVolume'
    '''
    Sets the volume setting of an input.
    
    Initial version: 5.0.0
    '''
    GET_INPUT_AUDIO_BALANCE = 'GetInputAudioBalance'
    '''
    Gets the audio balance of an input.
    
    Initial version: 5.0.0
    '''
    SET_INPUT_AUDIO_BALANCE = 'SetInputAudioBalance'
    '''
    Sets the audio balance of an input.
    
    Initial version: 5.0.0
    '''
    GET_INPUT_AUDIO_SYNC_OFFSET = 'GetInputAudioSyncOffset'
    '''
    Gets the audio sync offset of an input.
    
    Note: The audio sync offset can be negative too!
    
    Initial version: 5.0.0
    '''
    SET_INPUT_AUDIO_SYNC_OFFSET = 'SetInputAudioSyncOffset'
    '''
    Sets the audio sync offset of an input.
    
    Initial version: 5.0.0
    '''
    GET_INPUT_AUDIO_MONITOR_TYPE = 'GetInputAudioMonitorType'
    '''
    Gets the audio monitor type of an input.
    
    The available audio monitor types are:
    
    - `OBS_MONITORING_TYPE_NONE`
    - `OBS_MONITORING_TYPE_MONITOR_ONLY`
    - `OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT`
    
    Initial version: 5.0.0
    '''
    SET_INPUT_AUDIO_MONITOR_TYPE = 'SetInputAudioMonitorType'
    '''
    Sets the audio monitor type of an input.
    
    Initial version: 5.0.0
    '''
    GET_INPUT_AUDIO_TRACKS = 'GetInputAudioTracks'
    '''
    Gets the enable state of all audio tracks of an input.
    
    Initial version: 5.0.0
    '''
    SET_INPUT_AUDIO_TRACKS = 'SetInputAudioTracks'
    '''
    Sets the enable state of audio tracks of an input.
    
    Initial version: 5.0.0
    '''
    GET_INPUT_DEINTERLACE_MODE = 'GetInputDeinterlaceMode'
    '''
    Gets the deinterlace mode of an input.
    
    Deinterlace Modes:
    
    - `OBS_DEINTERLACE_MODE_DISABLE`
    - `OBS_DEINTERLACE_MODE_DISCARD`
    - `OBS_DEINTERLACE_MODE_RETRO`
    - `OBS_DEINTERLACE_MODE_BLEND`
    - `OBS_DEINTERLACE_MODE_BLEND_2X`
    - `OBS_DEINTERLACE_MODE_LINEAR`
    - `OBS_DEINTERLACE_MODE_LINEAR_2X`
    - `OBS_DEINTERLACE_MODE_YADIF`
    - `OBS_DEINTERLACE_MODE_YADIF_2X`
    
    Note: Deinterlacing functionality is restricted to async inputs only.
    
    Initial version: 5.6.0
    '''
    SET_INPUT_DEINTERLACE_MODE = 'SetInputDeinterlaceMode'
    '''
    Sets the deinterlace mode of an input.
    
    Note: Deinterlacing functionality is restricted to async inputs only.
    
    Initial version: 5.6.0
    '''
    GET_INPUT_DEINTERLACE_FIELD_ORDER = 'GetInputDeinterlaceFieldOrder'
    '''
    Gets the deinterlace field order of an input.
    
    Deinterlace Field Orders:
    
    - `OBS_DEINTERLACE_FIELD_ORDER_TOP`
    - `OBS_DEINTERLACE_FIELD_ORDER_BOTTOM`
    
    Note: Deinterlacing functionality is restricted to async inputs only.
    
    Initial version: 5.6.0
    '''
    SET_INPUT_DEINTERLACE_FIELD_ORDER = 'SetInputDeinterlaceFieldOrder'
    '''
    Sets the deinterlace field order of an input.
    
    Note: Deinterlacing functionality is restricted to async inputs only.
    
    Initial version: 5.6.0
    '''
    GET_INPUT_PROPERTIES_LIST_PROPERTY_ITEMS = 'GetInputPropertiesListPropertyItems'
    '''
    Gets the items of a list property from an input's properties.
    
    Note: Use this in cases where an input provides a dynamic, selectable list of items. For example, display capture, where it provides a list of available displays.
    
    Initial version: 5.0.0
    '''
    PRESS_INPUT_PROPERTIES_BUTTON = 'PressInputPropertiesButton'
    '''
    Presses a button in the properties of an input.
    
    Some known `propertyName` values are:
    
    - `refreshnocache` - Browser source reload button
    
    Note: Use this in cases where there is a button in the properties of an input that cannot be accessed in any other way. For example, browser sources, where there is a refresh button.
    
    Initial version: 5.0.0
    '''
    GET_MEDIA_INPUT_STATUS = 'GetMediaInputStatus'
    '''
    Gets the status of a media input.
    
    Media States:
    
    - `OBS_MEDIA_STATE_NONE`
    - `OBS_MEDIA_STATE_PLAYING`
    - `OBS_MEDIA_STATE_OPENING`
    - `OBS_MEDIA_STATE_BUFFERING`
    - `OBS_MEDIA_STATE_PAUSED`
    - `OBS_MEDIA_STATE_STOPPED`
    - `OBS_MEDIA_STATE_ENDED`
    - `OBS_MEDIA_STATE_ERROR`
    
    Initial version: 5.0.0
    '''
    SET_MEDIA_INPUT_CURSOR = 'SetMediaInputCursor'
    '''
    Sets the cursor position of a media input.
    
    This request does not perform bounds checking of the cursor position.
    
    Initial version: 5.0.0
    '''
    OFFSET_MEDIA_INPUT_CURSOR = 'OffsetMediaInputCursor'
    '''
    Offsets the current cursor position of a media input by the specified value.
    
    This request does not perform bounds checking of the cursor position.
    
    Initial version: 5.0.0
    '''
    TRIGGER_MEDIA_INPUT_ACTION = 'TriggerMediaInputAction'
    '''
    Triggers an action on a media input.
    
    Initial version: 5.0.0
    '''
    GET_VIRTUAL_CAM_STATUS = 'GetVirtualCamStatus'
    '''
    Gets the status of the virtualcam output.
    
    Initial version: 5.0.0
    '''
    TOGGLE_VIRTUAL_CAM = 'ToggleVirtualCam'
    '''
    Toggles the state of the virtualcam output.
    
    Initial version: 5.0.0
    '''
    START_VIRTUAL_CAM = 'StartVirtualCam'
    '''
    Starts the virtualcam output.
    
    Initial version: 5.0.0
    '''
    STOP_VIRTUAL_CAM = 'StopVirtualCam'
    '''
    Stops the virtualcam output.
    
    Initial version: 5.0.0
    '''
    GET_REPLAY_BUFFER_STATUS = 'GetReplayBufferStatus'
    '''
    Gets the status of the replay buffer output.
    
    Initial version: 5.0.0
    '''
    TOGGLE_REPLAY_BUFFER = 'ToggleReplayBuffer'
    '''
    Toggles the state of the replay buffer output.
    
    Initial version: 5.0.0
    '''
    START_REPLAY_BUFFER = 'StartReplayBuffer'
    '''
    Starts the replay buffer output.
    
    Initial version: 5.0.0
    '''
    STOP_REPLAY_BUFFER = 'StopReplayBuffer'
    '''
    Stops the replay buffer output.
    
    Initial version: 5.0.0
    '''
    SAVE_REPLAY_BUFFER = 'SaveReplayBuffer'
    '''
    Saves the contents of the replay buffer output.
    
    Initial version: 5.0.0
    '''
    GET_LAST_REPLAY_BUFFER_REPLAY = 'GetLastReplayBufferReplay'
    '''
    Gets the filename of the last replay buffer save file.
    
    Initial version: 5.0.0
    '''
    GET_OUTPUT_LIST = 'GetOutputList'
    '''
    Gets the list of available outputs.
    
    Initial version: 5.0.0
    '''
    GET_OUTPUT_STATUS = 'GetOutputStatus'
    '''
    Gets the status of an output.
    
    Initial version: 5.0.0
    '''
    TOGGLE_OUTPUT = 'ToggleOutput'
    '''
    Toggles the status of an output.
    
    Initial version: 5.0.0
    '''
    START_OUTPUT = 'StartOutput'
    '''
    Starts an output.
    
    Initial version: 5.0.0
    '''
    STOP_OUTPUT = 'StopOutput'
    '''
    Stops an output.
    
    Initial version: 5.0.0
    '''
    GET_OUTPUT_SETTINGS = 'GetOutputSettings'
    '''
    Gets the settings of an output.
    
    Initial version: 5.0.0
    '''
    SET_OUTPUT_SETTINGS = 'SetOutputSettings'
    '''
    Sets the settings of an output.
    
    Initial version: 5.0.0
    '''
    GET_RECORD_STATUS = 'GetRecordStatus'
    '''
    Gets the status of the record output.
    
    Initial version: 5.0.0
    '''
    TOGGLE_RECORD = 'ToggleRecord'
    '''
    Toggles the status of the record output.
    
    Initial version: 5.0.0
    '''
    START_RECORD = 'StartRecord'
    '''
    Starts the record output.
    
    Initial version: 5.0.0
    '''
    STOP_RECORD = 'StopRecord'
    '''
    Stops the record output.
    
    Initial version: 5.0.0
    '''
    TOGGLE_RECORD_PAUSE = 'ToggleRecordPause'
    '''
    Toggles pause on the record output.
    
    Initial version: 5.0.0
    '''
    PAUSE_RECORD = 'PauseRecord'
    '''
    Pauses the record output.
    
    Initial version: 5.0.0
    '''
    RESUME_RECORD = 'ResumeRecord'
    '''
    Resumes the record output.
    
    Initial version: 5.0.0
    '''
    SPLIT_RECORD_FILE = 'SplitRecordFile'
    '''
    Splits the current file being recorded into a new file.
    
    Initial version: 5.5.0
    '''
    CREATE_RECORD_CHAPTER = 'CreateRecordChapter'
    '''
    Adds a new chapter marker to the file currently being recorded.
    
    Note: As of OBS 30.2.0, the only file format supporting this feature is Hybrid MP4.
    
    Initial version: 5.5.0
    '''
    GET_SCENE_ITEM_LIST = 'GetSceneItemList'
    '''
    Gets a list of all scene items in a scene.
    
    Scenes only
    
    Initial version: 5.0.0
    '''
    GET_GROUP_SCENE_ITEM_LIST = 'GetGroupSceneItemList'
    '''
    Basically GetSceneItemList, but for groups.
    
    Using groups at all in OBS is discouraged, as they are very broken under the hood. Please use nested scenes instead.
    
    Groups only
    
    Initial version: 5.0.0
    '''
    GET_SCENE_ITEM_ID = 'GetSceneItemId'
    '''
    Searches a scene for a source, and returns its id.
    
    Scenes and Groups
    
    Initial version: 5.0.0
    '''
    GET_SCENE_ITEM_SOURCE = 'GetSceneItemSource'
    '''
    Gets the source associated with a scene item.
    
    Initial version: 5.4.0
    '''
    CREATE_SCENE_ITEM = 'CreateSceneItem'
    '''
    Creates a new scene item using a source.
    
    Scenes only
    
    Initial version: 5.0.0
    '''
    REMOVE_SCENE_ITEM = 'RemoveSceneItem'
    '''
    Removes a scene item from a scene.
    
    Scenes only
    
    Initial version: 5.0.0
    '''
    DUPLICATE_SCENE_ITEM = 'DuplicateSceneItem'
    '''
    Duplicates a scene item, copying all transform and crop info.
    
    Scenes only
    
    Initial version: 5.0.0
    '''
    GET_SCENE_ITEM_TRANSFORM = 'GetSceneItemTransform'
    '''
    Gets the transform and crop info of a scene item.
    
    Scenes and Groups
    
    Initial version: 5.0.0
    '''
    SET_SCENE_ITEM_TRANSFORM = 'SetSceneItemTransform'
    '''
    Sets the transform and crop info of a scene item.
    
    Initial version: 5.0.0
    '''
    GET_SCENE_ITEM_ENABLED = 'GetSceneItemEnabled'
    '''
    Gets the enable state of a scene item.
    
    Scenes and Groups
    
    Initial version: 5.0.0
    '''
    SET_SCENE_ITEM_ENABLED = 'SetSceneItemEnabled'
    '''
    Sets the enable state of a scene item.
    
    Scenes and Groups
    
    Initial version: 5.0.0
    '''
    GET_SCENE_ITEM_LOCKED = 'GetSceneItemLocked'
    '''
    Gets the lock state of a scene item.
    
    Scenes and Groups
    
    Initial version: 5.0.0
    '''
    SET_SCENE_ITEM_LOCKED = 'SetSceneItemLocked'
    '''
    Sets the lock state of a scene item.
    
    Scenes and Group
    
    Initial version: 5.0.0
    '''
    GET_SCENE_ITEM_INDEX = 'GetSceneItemIndex'
    '''
    Gets the index position of a scene item in a scene.
    
    An index of 0 is at the bottom of the source list in the UI.
    
    Scenes and Groups
    
    Initial version: 5.0.0
    '''
    SET_SCENE_ITEM_INDEX = 'SetSceneItemIndex'
    '''
    Sets the index position of a scene item in a scene.
    
    Scenes and Groups
    
    Initial version: 5.0.0
    '''
    GET_SCENE_ITEM_BLEND_MODE = 'GetSceneItemBlendMode'
    '''
    Gets the blend mode of a scene item.
    
    Blend modes:
    
    - `OBS_BLEND_NORMAL`
    - `OBS_BLEND_ADDITIVE`
    - `OBS_BLEND_SUBTRACT`
    - `OBS_BLEND_SCREEN`
    - `OBS_BLEND_MULTIPLY`
    - `OBS_BLEND_LIGHTEN`
    - `OBS_BLEND_DARKEN`
    
    Scenes and Groups
    
    Initial version: 5.0.0
    '''
    SET_SCENE_ITEM_BLEND_MODE = 'SetSceneItemBlendMode'
    '''
    Sets the blend mode of a scene item.
    
    Scenes and Groups
    
    Initial version: 5.0.0
    '''
    GET_SCENE_LIST = 'GetSceneList'
    '''
    Gets an array of scenes in OBS.
    
    Initial version: 5.0.0
    '''
    GET_GROUP_LIST = 'GetGroupList'
    '''
    Gets an array of all groups in OBS.
    
    Groups in OBS are actually scenes, but renamed and modified. In obs-websocket, we treat them as scenes where we can.
    
    Initial version: 5.0.0
    '''
    GET_CURRENT_PROGRAM_SCENE = 'GetCurrentProgramScene'
    '''
    Gets the current program scene.
    
    Note 1: This request is slated to have the `currentProgram`-prefixed fields removed from in an upcoming RPC version.
    
    Note 2: Canvases do not have any concept of a program or preview scene, so this request does not support canvases.
    
    Initial version: 5.0.0
    '''
    SET_CURRENT_PROGRAM_SCENE = 'SetCurrentProgramScene'
    '''
    Sets the current program scene.
    
    Initial version: 5.0.0
    '''
    GET_CURRENT_PREVIEW_SCENE = 'GetCurrentPreviewScene'
    '''
    Gets the current preview scene.
    
    Only available when studio mode is enabled.
    
    Note: This request is slated to have the `currentPreview`-prefixed fields removed from in an upcoming RPC version.
    
    Initial version: 5.0.0
    '''
    SET_CURRENT_PREVIEW_SCENE = 'SetCurrentPreviewScene'
    '''
    Sets the current preview scene.
    
    Only available when studio mode is enabled.
    
    Initial version: 5.0.0
    '''
    CREATE_SCENE = 'CreateScene'
    '''
    Creates a new scene in OBS.
    
    Initial version: 5.0.0
    '''
    REMOVE_SCENE = 'RemoveScene'
    '''
    Removes a scene from OBS.
    
    Initial version: 5.0.0
    '''
    SET_SCENE_NAME = 'SetSceneName'
    '''
    Sets the name of a scene (rename).
    
    Initial version: 5.0.0
    '''
    GET_SCENE_SCENE_TRANSITION_OVERRIDE = 'GetSceneSceneTransitionOverride'
    '''
    Gets the scene transition overridden for a scene.
    
    Note: A transition UUID response field is not currently able to be implemented as of 2024-1-18.
    
    Initial version: 5.0.0
    '''
    SET_SCENE_SCENE_TRANSITION_OVERRIDE = 'SetSceneSceneTransitionOverride'
    '''
    Sets the scene transition overridden for a scene.
    
    Initial version: 5.0.0
    '''
    GET_SOURCE_ACTIVE = 'GetSourceActive'
    '''
    Gets the active and show state of a source.
    
    **Compatible with inputs and scenes.**
    
    Initial version: 5.0.0
    '''
    GET_SOURCE_SCREENSHOT = 'GetSourceScreenshot'
    '''
    Gets a Base64-encoded screenshot of a source.
    
    The `imageWidth` and `imageHeight` parameters are treated as "scale to inner", meaning the smallest ratio will be used and the aspect ratio of the original resolution is kept.
    If `imageWidth` and `imageHeight` are not specified, the compressed image will use the full resolution of the source.
    
    **Compatible with inputs and scenes.**
    
    Initial version: 5.0.0
    '''
    SAVE_SOURCE_SCREENSHOT = 'SaveSourceScreenshot'
    '''
    Saves a screenshot of a source to the filesystem.
    
    The `imageWidth` and `imageHeight` parameters are treated as "scale to inner", meaning the smallest ratio will be used and the aspect ratio of the original resolution is kept.
    If `imageWidth` and `imageHeight` are not specified, the compressed image will use the full resolution of the source.
    
    **Compatible with inputs and scenes.**
    
    Initial version: 5.0.0
    '''
    GET_STREAM_STATUS = 'GetStreamStatus'
    '''
    Gets the status of the stream output.
    
    Initial version: 5.0.0
    '''
    TOGGLE_STREAM = 'ToggleStream'
    '''
    Toggles the status of the stream output.
    
    Initial version: 5.0.0
    '''
    START_STREAM = 'StartStream'
    '''
    Starts the stream output.
    
    Initial version: 5.0.0
    '''
    STOP_STREAM = 'StopStream'
    '''
    Stops the stream output.
    
    Initial version: 5.0.0
    '''
    SEND_STREAM_CAPTION = 'SendStreamCaption'
    '''
    Sends CEA-608 caption text over the stream output.
    
    Initial version: 5.0.0
    '''
    GET_TRANSITION_KIND_LIST = 'GetTransitionKindList'
    '''
    Gets an array of all available transition kinds.
    
    Similar to `GetInputKindList`
    
    Initial version: 5.0.0
    '''
    GET_SCENE_TRANSITION_LIST = 'GetSceneTransitionList'
    '''
    Gets an array of all scene transitions in OBS.
    
    Initial version: 5.0.0
    '''
    GET_CURRENT_SCENE_TRANSITION = 'GetCurrentSceneTransition'
    '''
    Gets information about the current scene transition.
    
    Initial version: 5.0.0
    '''
    SET_CURRENT_SCENE_TRANSITION = 'SetCurrentSceneTransition'
    '''
    Sets the current scene transition.
    
    Small note: While the namespace of scene transitions is generally unique, that uniqueness is not a guarantee as it is with other resources like inputs.
    
    Initial version: 5.0.0
    '''
    SET_CURRENT_SCENE_TRANSITION_DURATION = 'SetCurrentSceneTransitionDuration'
    '''
    Sets the duration of the current scene transition, if it is not fixed.
    
    Initial version: 5.0.0
    '''
    SET_CURRENT_SCENE_TRANSITION_SETTINGS = 'SetCurrentSceneTransitionSettings'
    '''
    Sets the settings of the current scene transition.
    
    Initial version: 5.0.0
    '''
    GET_CURRENT_SCENE_TRANSITION_CURSOR = 'GetCurrentSceneTransitionCursor'
    '''
    Gets the cursor position of the current scene transition.
    
    Note: `transitionCursor` will return 1.0 when the transition is inactive.
    
    Initial version: 5.0.0
    '''
    TRIGGER_STUDIO_MODE_TRANSITION = 'TriggerStudioModeTransition'
    '''
    Triggers the current scene transition. Same functionality as the `Transition` button in studio mode.
    
    Initial version: 5.0.0
    '''
    SET_TBAR_POSITION = 'SetTBarPosition'
    '''
    Sets the position of the TBar.
    
    **Very important note**: This will be deprecated and replaced in a future version of obs-websocket.
    
    Initial version: 5.0.0
    '''
    GET_STUDIO_MODE_ENABLED = 'GetStudioModeEnabled'
    '''
    Gets whether studio is enabled.
    
    Initial version: 5.0.0
    '''
    SET_STUDIO_MODE_ENABLED = 'SetStudioModeEnabled'
    '''
    Enables or disables studio mode
    
    Initial version: 5.0.0
    '''
    OPEN_INPUT_PROPERTIES_DIALOG = 'OpenInputPropertiesDialog'
    '''
    Opens the properties dialog of an input.
    
    Initial version: 5.0.0
    '''
    OPEN_INPUT_FILTERS_DIALOG = 'OpenInputFiltersDialog'
    '''
    Opens the filters dialog of an input.
    
    Initial version: 5.0.0
    '''
    OPEN_INPUT_INTERACT_DIALOG = 'OpenInputInteractDialog'
    '''
    Opens the interact dialog of an input.
    
    Initial version: 5.0.0
    '''
    GET_MONITOR_LIST = 'GetMonitorList'
    '''
    Gets a list of connected monitors and information about them.
    
    Initial version: 5.0.0
    '''
    OPEN_VIDEO_MIX_PROJECTOR = 'OpenVideoMixProjector'
    '''
    Opens a projector for a specific output video mix.
    
    Mix types:
    
    - `OBS_WEBSOCKET_VIDEO_MIX_TYPE_PREVIEW`
    - `OBS_WEBSOCKET_VIDEO_MIX_TYPE_PROGRAM`
    - `OBS_WEBSOCKET_VIDEO_MIX_TYPE_MULTIVIEW`
    
    Note: This request serves to provide feature parity with 4.x. It is very likely to be changed/deprecated in a future release.
    
    Initial version: 5.0.0
    '''
    OPEN_SOURCE_PROJECTOR = 'OpenSourceProjector'
    '''
    Opens a projector for a source.
    
    Note: This request serves to provide feature parity with 4.x. It is very likely to be changed/deprecated in a future release.
    
    Initial version: 5.0.0
    '''