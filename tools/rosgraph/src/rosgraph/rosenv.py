# Software License Agreement (BSD License)
#
# Copyright (c) 2009, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os
import sys

ROS_MASTER_URI   = "ROS_MASTER_URI"

ROS_IP           ="ROS_IP"
ROS_IPV6         ="ROS_IPV6"
ROS_HOSTNAME     ="ROS_HOSTNAME"
ROS_NAMESPACE    ="ROS_NAMESPACE"
ROS_UDS_EXT_FEATURE = "ROS_UDS_EXT_FEATURE"

# UDS Feature Bit Field
# Unix Domain Socket Feature Bit Field controlled by environmental value from user.
ROS_UDS_EXT_ABSTRACT_SOCK_NAME = 0x00000001  # enable abstract named socket

DEFAULT_MASTER_PORT = 11311  # default port for master's to bind to
DEFAULT_MASTER_URI = 'http://localhost:%s/' % DEFAULT_MASTER_PORT

def get_master_uri(env=None, argv=None):
    """
    Get the :envvar:`ROS_MASTER_URI` setting from the command-line args or
    environment, command-line args takes precedence.

    :param env: override environment dictionary, ``dict``
    :param argv: override ``sys.argv``, ``[str]``
    :raises: :exc:`ValueError` If :envvar:`ROS_MASTER_URI` value is invalidly
      specified 
    """    
    if env is None:
        env = os.environ
    if argv is None:
        argv = sys.argv
    
    for arg in argv:
        if arg.startswith('__master:='):
            val = None
            try:
                _, val = arg.split(':=')
            except:
                pass
            
            # we ignore required here because there really is no
            # correct return value as the configuration is bad
            # rather than unspecified
            if not val:
                raise ValueError("__master remapping argument '%s' improperly specified"%arg)
            return val
    return env.get(ROS_MASTER_URI, DEFAULT_MASTER_URI)
        
def ros_uds_ext_is_enable(feature):
    return ROS_UDS_EXT_FEATURE in os.environ and (int(os.environ[ROS_UDS_EXT_FEATURE], 16) & feature != 0)
