# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CanadianWebServicesDialog
                                 A QGIS plugin
 This plugin provides easy access to many geospatial web services in the Canadian (.ca) domain.
                             -------------------
        begin                : 2018-04-23
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Nathan Torrence
        email                : towence47@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import QtGui, uic 
from qgis.PyQt.QtWidgets import QDialog

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'canadian_web_services_dialog_base.ui'))


class CanadianWebServicesDialog(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(CanadianWebServicesDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
