# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CanadianWebServices
                                 A QGIS plugin
 This plugin provides easy access to many geospatial web services in the Canadian (.ca) domain.
                             -------------------
        begin                : 2018-04-23
        copyright            : (C) 2018 by Nathan Torrence
        email                : towence47@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CanadianWebServices class from file CanadianWebServices.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .canadian_web_services import CanadianWebServices
    return CanadianWebServices(iface)
