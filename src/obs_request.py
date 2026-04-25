from uuid import uuid4

from .obs_enums import RequestType, WebSocketOpCode
from .obs_schema import RequestMessage


class Request:
    """
    A request as a modifiable object.
    ### Arguments
    - `typ` - The request type.
    - `id` - The request ID. Directly returned in the response. Useful for distinguishing requests and queue manipulation.
    - `data` - Data, if any, required for the request.
    """

    def __init__(self, typ: RequestType, id: str = None, data=None):
        self.type = typ
        """
        The request type.
        """
        self.id = id or str(uuid4())
        """
        The request ID. Directly returned in the response. Useful for distinguishing requests and queue manipulation.
        """
        self.data = data
        """
        Data, if any, required for the request.
        """

    def build_data(self):
        """
        Build the request's data into a dictionary.
        ### Returns
        A [request data](https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#request-opcode-6) dictionary.
        """
        return {
            "requestType": self.type.value,
            "requestId": self.id,
            "requestData": self.data,
        }

    def build_message(self) -> RequestMessage:
        """
        Build the request into a dictionary ready to be sent to OBS.
        ### Returns
        A [request message](https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#request-opcode-6) dictionary.
        """
        return {
            "op": WebSocketOpCode.REQUEST,
            "d": self.build_data(),
        }
