# TD-OBSWebSocket

A packaged TouchDesigner component that connects to an [OBS](https://obsproject.com) WebSocket server and receives all available events.

## Usage

1. Download the .tox file from the `/dist` folder and place it in a location convenient for your project.
2. Drag and drop it into your project.
3. Set the Address and Port of the server in the Connection parameters tab. Set the Password if there is one.
4. If Auto-Reconnect is enabled: the component will connect to the server automatically.
   If Auto-Reconnect is disabled: enable the Active switch to connect to the server.

Several events are considered "high-volume" and must be individually opted into to receive them. You can do this in the Connection parameters tab. These events are:

- Input Volume Meters
- Input Active State Changed
- Input Show State Changed
- Scene Item Transform Changed

Once connected, any event data received will be set in the corresponding parameter. This makes the data easy to consume by, for example, connecting a Parameter Execute DAT to the OBSWebSocket COMP.

It's possible to enable or disable high-volume events while connected to the server. This will force a reconnect, however.

## Contributing

A custom Release component can be found in the project that automates the packaging, so simply make changes, increase the Version parameter (following [semver](https://semver.org)), and click the Release button.