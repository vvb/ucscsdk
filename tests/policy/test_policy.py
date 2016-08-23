# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from nose.tools import with_setup
from ..connection.info import custom_setup, custom_teardown

handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)


@with_setup(setup, teardown)
def test_001_policy():
    from ucscentralsdk.mometa.flowctrl.FlowctrlItem import FlowctrlItem

    # #####################################
    # Create a Flow Control Policy
    # #####################################
    mo = FlowctrlItem(parent_mo_or_dn="domaingroup-root/flowctrl", snd="off",
                      rcv="off", name="test", prio="on")
    handle.add_mo(mo)
    handle.commit()

    # #####################################
    # Delete Flow Control Policy
    # #####################################
    obj = handle.query_dn("domaingroup-root/flowctrl/policy-test")
    handle.remove_mo(obj)
    handle.commit()

    # #####################################
    # Create Dynamic vNIC Connection Policy
    # #####################################
    from ucscentralsdk.mometa.vnic.VnicDynamicConPolicy import VnicDynamicConPolicy

    mo = VnicDynamicConPolicy(parent_mo_or_dn="org-root", name="test",
                              descr="test", adaptor_profile_name="Linux",
                              protection="protected-pref-b", dynamic_eth="54")
    handle.add_mo(mo)
    handle.commit()

    # #####################################
    # Delete Dynamic vNIC Connection Policy
    # #####################################
    obj = handle.query_dn("org-root/dynamic-con-test")
    handle.remove_mo(obj)
    handle.commit()

    # #####################################
    # Create LACP Policy
    # #####################################
    from ucscentralsdk.mometa.fabric.FabricLacpPolicy import FabricLacpPolicy

    mo = FabricLacpPolicy(parent_mo_or_dn="domaingroup-root", fast_timer="fast",
                          suspend_individual="true",
                          name="test", descr="")
    handle.add_mo(mo)
    handle.commit()

    # #####################################
    # Modify LACP Policy
    # #####################################
    obj = handle.query_dn("domaingroup-root/lacp-test")
    obj.fast_timer = "normal"
    obj.suspend_individual = "false"
    obj.descr = ""
    handle.set_mo(obj)
    handle.commit()

    # #####################################
    # Delete LACP Policy
    # #####################################
    obj = handle.query_dn("domaingroup-root/lacp-test")
    handle.remove_mo(obj)
    handle.commit()

    # #####################################
    # Create LAN Connectivity Policy
    # #####################################
    from ucscentralsdk.mometa.vnic.VnicLanConnPolicy import VnicLanConnPolicy
    from ucscentralsdk.mometa.vnic.VnicEther import VnicEther
    from ucscentralsdk.mometa.vnic.VnicEtherIf import VnicEtherIf

    mo = VnicLanConnPolicy(parent_mo_or_dn="org-root",
                           name="test", descr="test_policy")
    mo_1 = VnicEther(parent_mo_or_dn=mo, nw_ctrl_policy_name="default",
                     name="test", admin_host_port="ANY", admin_vcon="any",
                     stats_policy_name="default", admin_cdn_name="",
                     switch_id="A", pin_to_group_name="", mtu="1500",
                     qos_policy_name="qos-1", adaptor_profile_name="Linux",
                     ident_pool_name="mac-pool-1", order="1", nw_templ_name="",
                     addr="derived")
    mo_1_1 = VnicEtherIf(parent_mo_or_dn=mo_1, default_net="yes",
                         name="default")
    handle.add_mo(mo)
    handle.commit()

    # #####################################
    # Delete LAN Connectivity Policy
    # #####################################
    obj = handle.query_dn("org-root/lan-conn-pol-test")
    handle.remove_mo(obj)
    handle.commit()

    # #####################################
    # Create QoS Policy
    # #####################################
    from ucscentralsdk.mometa.epqos.EpqosDefinition import EpqosDefinition
    from ucscentralsdk.mometa.epqos.EpqosEgress import EpqosEgress

    mo = EpqosDefinition(parent_mo_or_dn="org-root",
                         name="test", descr="")
    mo_1 = EpqosEgress(parent_mo_or_dn=mo, rate="line-rate",
                       host_control="none", name="", prio="best-effort",
                       burst="10240")
    handle.add_mo(mo)
    handle.commit()

    # #####################################
    # Delete QoS Policy
    # #####################################
    obj = handle.query_dn("org-root/ep-qos-test")
    handle.remove_mo(obj)
    handle.commit()
