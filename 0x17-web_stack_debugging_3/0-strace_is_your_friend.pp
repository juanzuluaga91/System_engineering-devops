# fix
exec { 'sed -ie \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php':
  command => '/bin/sed -ie \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php',
}

exec { 'service apache2 restart':
  command => '/usr/sbin/service apache2 restart',
}
