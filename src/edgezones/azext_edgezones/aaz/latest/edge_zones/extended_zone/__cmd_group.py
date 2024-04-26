# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "edge-zones extended-zone",
    is_preview=True,
)
class __CMDGroup(AAZCommandGroup):
    """A small-footprint extension of Azure.

    Azure Extended Zones are small-footprint extensions of Azure placed in metros, industry centers, or a specific jurisdiction to serve low latency and/or data residency workloads.
    """
    pass


__all__ = ["__CMDGroup"]