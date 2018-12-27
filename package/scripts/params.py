#!/usr/bin/env python

import os
from resource_management import *
from resource_management.libraries.script.script import Script

config = Script.get_config()

# others conf
hdfs_default_fs = default("/configurations/core-site/fs.defaultFS", '')

## drill-ambari-config.xml
drill_install_dir = config['configurations']['drill-ambari-config']['drill_install_dir']
drill_temp_file = config['configurations']['drill-ambari-config']['drill_temp_file']
hadoop_core_site = config['configurations']['drill-ambari-config']['hadoop_core_site']
hadoop_hdfs_site = config['configurations']['drill-ambari-config']['hadoop_hdfs_site']
#drill_pid_file = os.path.join(drill_install_dir,'apache-drill-1.14.0','drillbit.pid')
drill_pid_file = '/opt/apache-drill/apache-drill-1.14.0/drillbit.pid'

## drill-env.xml
drill_user = config['configurations']['drill-env']['drill_user']
drill_group = config['configurations']['drill-env']['drill_group']
drill_max_direct_memory = config['configurations']['drill-env']['drill_max_direct_memory']
drill_heap_size = config['configurations']['drill-env']['drill_heap_size']
drill_log_dir = config['configurations']['drill-env']['drill_log_dir']
drill_env_content = config['configurations']['drill-env']['content']
drill_log_file = os.path.join(drill_log_dir,'drill-install.log')


## drill-override.xml
cluster_id = config['configurations']['drill-override']['cluster_id']
zk_connect = config['configurations']['drill-override']['zk_connect']
sys_store_provider_zk_blobroot = config['configurations']['drill-override']['sys_store_provider_zk_blobroot']
drill_override_content = config['configurations']['drill-override']['content']


