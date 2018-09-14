## Synopsis

Discovery of relevant datasets remains a key barrier to the uptake of use of GIS for decision-making.  The GeoConnections program at Natural Resources Canada is working to address this.
Fundamental to this is encouraging the use of standards and completion of accurate metadata.
This plugin is a aid to viewing Canadian web services (see below for what types) that are open and available.  It currently is populated with a list of services harvested weekly from the .ca landscape.
It then allows the user to efficiently add all layers of each service and retain the service connection in the user profile for later use.

## Usage

1. Open Plugin.
2. Wait for service list to be populated over the internet.
3. Filter
4. Select, or <ctrl> select items to load layers from.
5. Click 'load' to populate your project file.

### Installation:

1.  Download files found at [https://github.com/eswright/cgdi-qgis-services](https://github.com/eswright/cgdi-qgis-services)
2.  Convert the folder named CanadianWebServices into a zip
3.  Open up Qgis Desktop 3.0 or higher
4.  Go to **Plugins > Manage and Install Plugins... > Install from ZIP**
5.  Choose the newly created zip file, and click install
6.  Once installed, ensure that you have checked **Show also experimental plugins** found at **Plugins > Manage and Install Plugins... > Settings**
7.  Finally, go to **Plugins > Manage and Install Plugins... > Installed** and make sure **Canadian Web Services** is checked

### Notes:

*   You can find the plugin in: C:\Users\**USER**\AppData\Roaming\QGIS\QGIS3\profiles\python\plugins\CanadianWebServices (where **USER** is your user profile name)
*   Once this plugin is added to the official Qgis repository ( in the experimental category), you can ignore the steps shown above, and install this plugin as you would with any other experimental plugin.



## Contributors
Nathan Torrence
Aayush Dobriyal
Eric Wright



## License

MIT
```
```