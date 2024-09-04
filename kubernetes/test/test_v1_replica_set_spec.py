# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_replica_set_spec import V1ReplicaSetSpec

class TestV1ReplicaSetSpec(unittest.TestCase):
    """V1ReplicaSetSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ReplicaSetSpec:
        """Test V1ReplicaSetSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ReplicaSetSpec`
        """
        model = V1ReplicaSetSpec()
        if include_optional:
            return V1ReplicaSetSpec(
                min_ready_seconds = 56,
                replicas = 56,
                selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                    match_expressions = [
                        kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                            key = '', 
                            operator = '', 
                            values = [
                                ''
                                ], )
                        ], 
                    match_labels = {
                        'key' : ''
                        }, ),
                template = kubernetes.client.models.v1/pod_template_spec.v1.PodTemplateSpec(
                    metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                        annotations = {
                            'key' : ''
                            }, 
                        creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        deletion_grace_period_seconds = 56, 
                        deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        finalizers = [
                            ''
                            ], 
                        generate_name = '', 
                        generation = 56, 
                        labels = {
                            'key' : ''
                            }, 
                        managed_fields = [
                            kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                api_version = '', 
                                fields_type = '', 
                                fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                manager = '', 
                                operation = '', 
                                subresource = '', 
                                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        name = '', 
                        namespace = '', 
                        owner_references = [
                            kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                api_version = '', 
                                block_owner_deletion = True, 
                                controller = True, 
                                kind = '', 
                                name = '', 
                                uid = '', )
                            ], 
                        resource_version = '', 
                        self_link = '', 
                        uid = '', ), 
                    spec = kubernetes.client.models.v1/pod_spec.v1.PodSpec(
                        active_deadline_seconds = 56, 
                        affinity = kubernetes.client.models.v1/affinity.v1.Affinity(
                            node_affinity = kubernetes.client.models.v1/node_affinity.v1.NodeAffinity(
                                preferred_during_scheduling_ignored_during_execution = [
                                    kubernetes.client.models.v1/preferred_scheduling_term.v1.PreferredSchedulingTerm(
                                        preference = kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm(
                                            match_expressions = [
                                                kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                                    key = '', 
                                                    operator = '', 
                                                    values = [
                                                        ''
                                                        ], )
                                                ], 
                                            match_fields = [
                                                kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                                    key = '', 
                                                    operator = '', )
                                                ], ), 
                                        weight = 56, )
                                    ], 
                                required_during_scheduling_ignored_during_execution = kubernetes.client.models.v1/node_selector.v1.NodeSelector(
                                    node_selector_terms = [
                                        kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm()
                                        ], ), ), 
                            pod_affinity = kubernetes.client.models.v1/pod_affinity.v1.PodAffinity(), 
                            pod_anti_affinity = kubernetes.client.models.v1/pod_anti_affinity.v1.PodAntiAffinity(), ), 
                        automount_service_account_token = True, 
                        containers = [
                            kubernetes.client.models.v1/container.v1.Container(
                                args = [
                                    ''
                                    ], 
                                command = [
                                    ''
                                    ], 
                                env = [
                                    kubernetes.client.models.v1/env_var.v1.EnvVar(
                                        name = '', 
                                        value = '', 
                                        value_from = kubernetes.client.models.v1/env_var_source.v1.EnvVarSource(
                                            config_map_key_ref = kubernetes.client.models.v1/config_map_key_selector.v1.ConfigMapKeySelector(
                                                key = '', 
                                                name = '', 
                                                optional = True, ), 
                                            field_ref = kubernetes.client.models.v1/object_field_selector.v1.ObjectFieldSelector(
                                                api_version = '', 
                                                field_path = '', ), 
                                            resource_field_ref = kubernetes.client.models.v1/resource_field_selector.v1.ResourceFieldSelector(
                                                container_name = '', 
                                                divisor = '', 
                                                resource = '', ), 
                                            secret_key_ref = kubernetes.client.models.v1/secret_key_selector.v1.SecretKeySelector(
                                                key = '', 
                                                name = '', 
                                                optional = True, ), ), )
                                    ], 
                                env_from = [
                                    kubernetes.client.models.v1/env_from_source.v1.EnvFromSource(
                                        config_map_ref = kubernetes.client.models.v1/config_map_env_source.v1.ConfigMapEnvSource(
                                            name = '', 
                                            optional = True, ), 
                                        prefix = '', 
                                        secret_ref = kubernetes.client.models.v1/secret_env_source.v1.SecretEnvSource(
                                            name = '', 
                                            optional = True, ), )
                                    ], 
                                image = '', 
                                image_pull_policy = '', 
                                lifecycle = kubernetes.client.models.v1/lifecycle.v1.Lifecycle(
                                    post_start = kubernetes.client.models.v1/lifecycle_handler.v1.LifecycleHandler(
                                        exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(), 
                                        http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                                            host = '', 
                                            http_headers = [
                                                kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                                                    name = '', 
                                                    value = '', )
                                                ], 
                                            path = '', 
                                            port = kubernetes.client.models.port.port(), 
                                            scheme = '', ), 
                                        sleep = kubernetes.client.models.v1/sleep_action.v1.SleepAction(
                                            seconds = 56, ), 
                                        tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                                            host = '', 
                                            port = kubernetes.client.models.port.port(), ), ), 
                                    pre_stop = kubernetes.client.models.v1/lifecycle_handler.v1.LifecycleHandler(), ), 
                                liveness_probe = kubernetes.client.models.v1/probe.v1.Probe(
                                    failure_threshold = 56, 
                                    grpc = kubernetes.client.models.v1/grpc_action.v1.GRPCAction(
                                        port = 56, 
                                        service = '', ), 
                                    initial_delay_seconds = 56, 
                                    period_seconds = 56, 
                                    success_threshold = 56, 
                                    termination_grace_period_seconds = 56, 
                                    timeout_seconds = 56, ), 
                                name = '', 
                                ports = [
                                    kubernetes.client.models.v1/container_port.v1.ContainerPort(
                                        container_port = 56, 
                                        host_ip = '', 
                                        host_port = 56, 
                                        name = '', 
                                        protocol = '', )
                                    ], 
                                readiness_probe = kubernetes.client.models.v1/probe.v1.Probe(
                                    failure_threshold = 56, 
                                    initial_delay_seconds = 56, 
                                    period_seconds = 56, 
                                    success_threshold = 56, 
                                    termination_grace_period_seconds = 56, 
                                    timeout_seconds = 56, ), 
                                resize_policy = [
                                    kubernetes.client.models.v1/container_resize_policy.v1.ContainerResizePolicy(
                                        resource_name = '', 
                                        restart_policy = '', )
                                    ], 
                                resources = kubernetes.client.models.v1/resource_requirements.v1.ResourceRequirements(
                                    claims = [
                                        kubernetes.client.models.v1/resource_claim.v1.ResourceClaim(
                                            name = '', 
                                            request = '', )
                                        ], 
                                    limits = {
                                        'key' : ''
                                        }, 
                                    requests = {
                                        'key' : ''
                                        }, ), 
                                restart_policy = '', 
                                security_context = kubernetes.client.models.v1/security_context.v1.SecurityContext(
                                    allow_privilege_escalation = True, 
                                    app_armor_profile = kubernetes.client.models.v1/app_armor_profile.v1.AppArmorProfile(
                                        localhost_profile = '', 
                                        type = '', ), 
                                    capabilities = kubernetes.client.models.v1/capabilities.v1.Capabilities(
                                        add = [
                                            ''
                                            ], 
                                        drop = [
                                            ''
                                            ], ), 
                                    privileged = True, 
                                    proc_mount = '', 
                                    read_only_root_filesystem = True, 
                                    run_as_group = 56, 
                                    run_as_non_root = True, 
                                    run_as_user = 56, 
                                    se_linux_options = kubernetes.client.models.v1/se_linux_options.v1.SELinuxOptions(
                                        level = '', 
                                        role = '', 
                                        type = '', 
                                        user = '', ), 
                                    seccomp_profile = kubernetes.client.models.v1/seccomp_profile.v1.SeccompProfile(
                                        localhost_profile = '', 
                                        type = '', ), 
                                    windows_options = kubernetes.client.models.v1/windows_security_context_options.v1.WindowsSecurityContextOptions(
                                        gmsa_credential_spec = '', 
                                        gmsa_credential_spec_name = '', 
                                        host_process = True, 
                                        run_as_user_name = '', ), ), 
                                startup_probe = , 
                                stdin = True, 
                                stdin_once = True, 
                                termination_message_path = '', 
                                termination_message_policy = '', 
                                tty = True, 
                                volume_devices = [
                                    kubernetes.client.models.v1/volume_device.v1.VolumeDevice(
                                        device_path = '', 
                                        name = '', )
                                    ], 
                                volume_mounts = [
                                    kubernetes.client.models.v1/volume_mount.v1.VolumeMount(
                                        mount_path = '', 
                                        mount_propagation = '', 
                                        name = '', 
                                        read_only = True, 
                                        recursive_read_only = '', 
                                        sub_path = '', 
                                        sub_path_expr = '', )
                                    ], 
                                working_dir = '', )
                            ], 
                        dns_config = kubernetes.client.models.v1/pod_dns_config.v1.PodDNSConfig(
                            nameservers = [
                                ''
                                ], 
                            options = [
                                kubernetes.client.models.v1/pod_dns_config_option.v1.PodDNSConfigOption(
                                    name = '', 
                                    value = '', )
                                ], 
                            searches = [
                                ''
                                ], ), 
                        dns_policy = '', 
                        enable_service_links = True, 
                        ephemeral_containers = [
                            kubernetes.client.models.v1/ephemeral_container.v1.EphemeralContainer(
                                image = '', 
                                image_pull_policy = '', 
                                name = '', 
                                restart_policy = '', 
                                stdin = True, 
                                stdin_once = True, 
                                target_container_name = '', 
                                termination_message_path = '', 
                                termination_message_policy = '', 
                                tty = True, 
                                working_dir = '', )
                            ], 
                        host_aliases = [
                            kubernetes.client.models.v1/host_alias.v1.HostAlias(
                                hostnames = [
                                    ''
                                    ], 
                                ip = '', )
                            ], 
                        host_ipc = True, 
                        host_network = True, 
                        host_pid = True, 
                        host_users = True, 
                        hostname = '', 
                        image_pull_secrets = [
                            kubernetes.client.models.v1/local_object_reference.v1.LocalObjectReference(
                                name = '', )
                            ], 
                        init_containers = [
                            kubernetes.client.models.v1/container.v1.Container(
                                image = '', 
                                image_pull_policy = '', 
                                name = '', 
                                restart_policy = '', 
                                stdin = True, 
                                stdin_once = True, 
                                termination_message_path = '', 
                                termination_message_policy = '', 
                                tty = True, 
                                working_dir = '', )
                            ], 
                        node_name = '', 
                        node_selector = {
                            'key' : ''
                            }, 
                        os = kubernetes.client.models.v1/pod_os.v1.PodOS(
                            name = '', ), 
                        overhead = {
                            'key' : ''
                            }, 
                        preemption_policy = '', 
                        priority = 56, 
                        priority_class_name = '', 
                        readiness_gates = [
                            kubernetes.client.models.v1/pod_readiness_gate.v1.PodReadinessGate(
                                condition_type = '', )
                            ], 
                        resource_claims = [
                            kubernetes.client.models.v1/pod_resource_claim.v1.PodResourceClaim(
                                name = '', 
                                resource_claim_name = '', 
                                resource_claim_template_name = '', )
                            ], 
                        restart_policy = '', 
                        runtime_class_name = '', 
                        scheduler_name = '', 
                        scheduling_gates = [
                            kubernetes.client.models.v1/pod_scheduling_gate.v1.PodSchedulingGate(
                                name = '', )
                            ], 
                        security_context = kubernetes.client.models.v1/pod_security_context.v1.PodSecurityContext(
                            fs_group = 56, 
                            fs_group_change_policy = '', 
                            run_as_group = 56, 
                            run_as_non_root = True, 
                            run_as_user = 56, 
                            supplemental_groups = [
                                56
                                ], 
                            supplemental_groups_policy = '', 
                            sysctls = [
                                kubernetes.client.models.v1/sysctl.v1.Sysctl(
                                    name = '', 
                                    value = '', )
                                ], ), 
                        service_account = '', 
                        service_account_name = '', 
                        set_hostname_as_fqdn = True, 
                        share_process_namespace = True, 
                        subdomain = '', 
                        termination_grace_period_seconds = 56, 
                        tolerations = [
                            kubernetes.client.models.v1/toleration.v1.Toleration(
                                effect = '', 
                                key = '', 
                                operator = '', 
                                toleration_seconds = 56, 
                                value = '', )
                            ], 
                        topology_spread_constraints = [
                            kubernetes.client.models.v1/topology_spread_constraint.v1.TopologySpreadConstraint(
                                label_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                                    match_labels = {
                                        'key' : ''
                                        }, ), 
                                match_label_keys = [
                                    ''
                                    ], 
                                max_skew = 56, 
                                min_domains = 56, 
                                node_affinity_policy = '', 
                                node_taints_policy = '', 
                                topology_key = '', 
                                when_unsatisfiable = '', )
                            ], 
                        volumes = [
                            kubernetes.client.models.v1/volume.v1.Volume(
                                aws_elastic_block_store = kubernetes.client.models.v1/aws_elastic_block_store_volume_source.v1.AWSElasticBlockStoreVolumeSource(
                                    fs_type = '', 
                                    partition = 56, 
                                    read_only = True, 
                                    volume_id = '', ), 
                                azure_disk = kubernetes.client.models.v1/azure_disk_volume_source.v1.AzureDiskVolumeSource(
                                    caching_mode = '', 
                                    disk_name = '', 
                                    disk_uri = '', 
                                    fs_type = '', 
                                    kind = '', 
                                    read_only = True, ), 
                                azure_file = kubernetes.client.models.v1/azure_file_volume_source.v1.AzureFileVolumeSource(
                                    read_only = True, 
                                    secret_name = '', 
                                    share_name = '', ), 
                                cephfs = kubernetes.client.models.v1/ceph_fs_volume_source.v1.CephFSVolumeSource(
                                    monitors = [
                                        ''
                                        ], 
                                    path = '', 
                                    read_only = True, 
                                    secret_file = '', 
                                    user = '', ), 
                                cinder = kubernetes.client.models.v1/cinder_volume_source.v1.CinderVolumeSource(
                                    fs_type = '', 
                                    read_only = True, 
                                    volume_id = '', ), 
                                config_map = kubernetes.client.models.v1/config_map_volume_source.v1.ConfigMapVolumeSource(
                                    default_mode = 56, 
                                    items = [
                                        kubernetes.client.models.v1/key_to_path.v1.KeyToPath(
                                            key = '', 
                                            mode = 56, 
                                            path = '', )
                                        ], 
                                    name = '', 
                                    optional = True, ), 
                                csi = kubernetes.client.models.v1/csi_volume_source.v1.CSIVolumeSource(
                                    driver = '', 
                                    fs_type = '', 
                                    node_publish_secret_ref = kubernetes.client.models.v1/local_object_reference.v1.LocalObjectReference(
                                        name = '', ), 
                                    read_only = True, 
                                    volume_attributes = {
                                        'key' : ''
                                        }, ), 
                                downward_api = kubernetes.client.models.v1/downward_api_volume_source.v1.DownwardAPIVolumeSource(
                                    default_mode = 56, ), 
                                empty_dir = kubernetes.client.models.v1/empty_dir_volume_source.v1.EmptyDirVolumeSource(
                                    medium = '', 
                                    size_limit = '', ), 
                                ephemeral = kubernetes.client.models.v1/ephemeral_volume_source.v1.EphemeralVolumeSource(
                                    volume_claim_template = kubernetes.client.models.v1/persistent_volume_claim_template.v1.PersistentVolumeClaimTemplate(
                                        spec = kubernetes.client.models.v1/persistent_volume_claim_spec.v1.PersistentVolumeClaimSpec(
                                            access_modes = [
                                                ''
                                                ], 
                                            data_source = kubernetes.client.models.v1/typed_local_object_reference.v1.TypedLocalObjectReference(
                                                api_group = '', 
                                                kind = '', 
                                                name = '', ), 
                                            data_source_ref = kubernetes.client.models.v1/typed_object_reference.v1.TypedObjectReference(
                                                api_group = '', 
                                                kind = '', 
                                                name = '', 
                                                namespace = '', ), 
                                            selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(), 
                                            storage_class_name = '', 
                                            volume_attributes_class_name = '', 
                                            volume_mode = '', 
                                            volume_name = '', ), ), ), 
                                fc = kubernetes.client.models.v1/fc_volume_source.v1.FCVolumeSource(
                                    fs_type = '', 
                                    lun = 56, 
                                    read_only = True, 
                                    target_wwns = [
                                        ''
                                        ], 
                                    wwids = [
                                        ''
                                        ], ), 
                                flex_volume = kubernetes.client.models.v1/flex_volume_source.v1.FlexVolumeSource(
                                    driver = '', 
                                    fs_type = '', 
                                    read_only = True, ), 
                                flocker = kubernetes.client.models.v1/flocker_volume_source.v1.FlockerVolumeSource(
                                    dataset_name = '', 
                                    dataset_uuid = '', ), 
                                gce_persistent_disk = kubernetes.client.models.v1/gce_persistent_disk_volume_source.v1.GCEPersistentDiskVolumeSource(
                                    fs_type = '', 
                                    partition = 56, 
                                    pd_name = '', 
                                    read_only = True, ), 
                                git_repo = kubernetes.client.models.v1/git_repo_volume_source.v1.GitRepoVolumeSource(
                                    directory = '', 
                                    repository = '', 
                                    revision = '', ), 
                                glusterfs = kubernetes.client.models.v1/glusterfs_volume_source.v1.GlusterfsVolumeSource(
                                    endpoints = '', 
                                    path = '', 
                                    read_only = True, ), 
                                host_path = kubernetes.client.models.v1/host_path_volume_source.v1.HostPathVolumeSource(
                                    path = '', 
                                    type = '', ), 
                                image = kubernetes.client.models.v1/image_volume_source.v1.ImageVolumeSource(
                                    pull_policy = '', 
                                    reference = '', ), 
                                iscsi = kubernetes.client.models.v1/iscsi_volume_source.v1.ISCSIVolumeSource(
                                    chap_auth_discovery = True, 
                                    chap_auth_session = True, 
                                    fs_type = '', 
                                    initiator_name = '', 
                                    iqn = '', 
                                    iscsi_interface = '', 
                                    lun = 56, 
                                    portals = [
                                        ''
                                        ], 
                                    read_only = True, 
                                    target_portal = '', ), 
                                name = '', 
                                nfs = kubernetes.client.models.v1/nfs_volume_source.v1.NFSVolumeSource(
                                    path = '', 
                                    read_only = True, 
                                    server = '', ), 
                                persistent_volume_claim = kubernetes.client.models.v1/persistent_volume_claim_volume_source.v1.PersistentVolumeClaimVolumeSource(
                                    claim_name = '', 
                                    read_only = True, ), 
                                photon_persistent_disk = kubernetes.client.models.v1/photon_persistent_disk_volume_source.v1.PhotonPersistentDiskVolumeSource(
                                    fs_type = '', 
                                    pd_id = '', ), 
                                portworx_volume = kubernetes.client.models.v1/portworx_volume_source.v1.PortworxVolumeSource(
                                    fs_type = '', 
                                    read_only = True, 
                                    volume_id = '', ), 
                                projected = kubernetes.client.models.v1/projected_volume_source.v1.ProjectedVolumeSource(
                                    default_mode = 56, 
                                    sources = [
                                        kubernetes.client.models.v1/volume_projection.v1.VolumeProjection(
                                            cluster_trust_bundle = kubernetes.client.models.v1/cluster_trust_bundle_projection.v1.ClusterTrustBundleProjection(
                                                name = '', 
                                                optional = True, 
                                                path = '', 
                                                signer_name = '', ), 
                                            secret = kubernetes.client.models.v1/secret_projection.v1.SecretProjection(
                                                name = '', 
                                                optional = True, ), 
                                            service_account_token = kubernetes.client.models.v1/service_account_token_projection.v1.ServiceAccountTokenProjection(
                                                audience = '', 
                                                expiration_seconds = 56, 
                                                path = '', ), )
                                        ], ), 
                                quobyte = kubernetes.client.models.v1/quobyte_volume_source.v1.QuobyteVolumeSource(
                                    group = '', 
                                    read_only = True, 
                                    registry = '', 
                                    tenant = '', 
                                    user = '', 
                                    volume = '', ), 
                                rbd = kubernetes.client.models.v1/rbd_volume_source.v1.RBDVolumeSource(
                                    fs_type = '', 
                                    image = '', 
                                    keyring = '', 
                                    monitors = [
                                        ''
                                        ], 
                                    pool = '', 
                                    read_only = True, 
                                    user = '', ), 
                                scale_io = kubernetes.client.models.v1/scale_io_volume_source.v1.ScaleIOVolumeSource(
                                    fs_type = '', 
                                    gateway = '', 
                                    protection_domain = '', 
                                    read_only = True, 
                                    secret_ref = , 
                                    ssl_enabled = True, 
                                    storage_mode = '', 
                                    storage_pool = '', 
                                    system = '', 
                                    volume_name = '', ), 
                                secret = kubernetes.client.models.v1/secret_volume_source.v1.SecretVolumeSource(
                                    default_mode = 56, 
                                    optional = True, 
                                    secret_name = '', ), 
                                storageos = kubernetes.client.models.v1/storage_os_volume_source.v1.StorageOSVolumeSource(
                                    fs_type = '', 
                                    read_only = True, 
                                    volume_name = '', 
                                    volume_namespace = '', ), 
                                vsphere_volume = kubernetes.client.models.v1/vsphere_virtual_disk_volume_source.v1.VsphereVirtualDiskVolumeSource(
                                    fs_type = '', 
                                    storage_policy_id = '', 
                                    storage_policy_name = '', 
                                    volume_path = '', ), )
                            ], ), )
            )
        else:
            return V1ReplicaSetSpec(
                selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                    match_expressions = [
                        kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                            key = '', 
                            operator = '', 
                            values = [
                                ''
                                ], )
                        ], 
                    match_labels = {
                        'key' : ''
                        }, ),
        )
        """

    def testV1ReplicaSetSpec(self):
        """Test V1ReplicaSetSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
