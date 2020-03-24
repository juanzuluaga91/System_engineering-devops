# PUPPET
exec { '/etc/ssh/ssh_config':
  command => '/bin/echo -e "IdentityFile ~/.ssh/holberton\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/etc/ssh/ssh_config',
}
