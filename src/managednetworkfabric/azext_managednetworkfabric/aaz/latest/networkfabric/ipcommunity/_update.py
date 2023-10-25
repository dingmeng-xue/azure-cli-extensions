# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "networkfabric ipcommunity update",
)
class Update(AAZCommand):
    """Update to update certain properties of the IP Community resource.

    :example: Update IP Community
        az networkfabric ipcommunity update --resource-group "example-rg" --resource-name "example-ipcommunity" --ip-community-rules "[{action:Permit,communityMembers:['1:1'],sequenceNumber:1234,wellKnownCommunities:[Internet,GShut]}]"
    """

    _aaz_info = {
        "version": "2023-06-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/ipcommunities/{}", "2023-06-15"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="Name of the IP Community.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the resource group",
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Body",
            help="Resource tags",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.ip_community_rules = AAZListArg(
            options=["--ip-community-rules"],
            arg_group="Properties",
            help="List of IP Community Rules.",
        )

        ip_community_rules = cls._args_schema.ip_community_rules
        ip_community_rules.Element = AAZObjectArg()

        _element = cls._args_schema.ip_community_rules.Element
        _element.action = AAZStrArg(
            options=["action"],
            help="Action to be taken on the configuration. Example: Permit.",
            required=True,
            enum={"Deny": "Deny", "Permit": "Permit"},
        )
        _element.community_members = AAZListArg(
            options=["community-members"],
            help="List the community members of IP Community.",
            required=True,
        )
        _element.sequence_number = AAZIntArg(
            options=["sequence-number"],
            help="Sequence to insert to/delete from existing route. Prefix lists are evaluated starting with the lowest sequence number and continue down the list until a match is made. Once a match is made, the permit or deny statement is applied to that network and the rest of the list is ignored.",
            required=True,
            fmt=AAZIntArgFormat(
                maximum=4294967295,
                minimum=1,
            ),
        )
        _element.well_known_communities = AAZListArg(
            options=["well-known-communities"],
            help="Supported well known Community List.",
            fmt=AAZListArgFormat(
                unique=True,
            ),
        )

        community_members = cls._args_schema.ip_community_rules.Element.community_members
        community_members.Element = AAZStrArg(
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )

        well_known_communities = cls._args_schema.ip_community_rules.Element.well_known_communities
        well_known_communities.Element = AAZStrArg(
            enum={"GShut": "GShut", "Internet": "Internet", "LocalAS": "LocalAS", "NoAdvertise": "NoAdvertise", "NoExport": "NoExport"},
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.IpCommunitiesUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class IpCommunitiesUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/ipCommunities/{ipCommunityName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PATCH"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "ipCommunityName", self.ctx.args.resource_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-06-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("ipCommunityRules", AAZListType, ".ip_community_rules")

            ip_community_rules = _builder.get(".properties.ipCommunityRules")
            if ip_community_rules is not None:
                ip_community_rules.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.ipCommunityRules[]")
            if _elements is not None:
                _elements.set_prop("action", AAZStrType, ".action", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("communityMembers", AAZListType, ".community_members", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("sequenceNumber", AAZIntType, ".sequence_number", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("wellKnownCommunities", AAZListType, ".well_known_communities")

            community_members = _builder.get(".properties.ipCommunityRules[].communityMembers")
            if community_members is not None:
                community_members.set_elements(AAZStrType, ".")

            well_known_communities = _builder.get(".properties.ipCommunityRules[].wellKnownCommunities")
            if well_known_communities is not None:
                well_known_communities.set_elements(AAZStrType, ".")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            properties.annotation = AAZStrType()
            properties.configuration_state = AAZStrType(
                serialized_name="configurationState",
                flags={"read_only": True},
            )
            properties.ip_community_rules = AAZListType(
                serialized_name="ipCommunityRules",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            ip_community_rules = cls._schema_on_200.properties.ip_community_rules
            ip_community_rules.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.ip_community_rules.Element
            _element.action = AAZStrType(
                flags={"required": True},
            )
            _element.community_members = AAZListType(
                serialized_name="communityMembers",
                flags={"required": True},
            )
            _element.sequence_number = AAZIntType(
                serialized_name="sequenceNumber",
                flags={"required": True},
            )
            _element.well_known_communities = AAZListType(
                serialized_name="wellKnownCommunities",
            )

            community_members = cls._schema_on_200.properties.ip_community_rules.Element.community_members
            community_members.Element = AAZStrType()

            well_known_communities = cls._schema_on_200.properties.ip_community_rules.Element.well_known_communities
            well_known_communities.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _UpdateHelper:
    """Helper class for Update"""


__all__ = ["Update"]