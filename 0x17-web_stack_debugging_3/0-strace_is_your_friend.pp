# Puppet function to rename phpp file to php
exec { 'Fix phpp file':
    command => "'sed -i 's|phpp|php|' /var/www/html/wp-settings.php",
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:'
}
