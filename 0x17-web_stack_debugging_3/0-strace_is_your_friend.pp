<<<<<<< HEAD
# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.
=======
# This Puppet code replaces the string "phpp" with "php" in the wp-settings.php file
>>>>>>> 6ac6b03da8638e6f572637a1d3b3f26653ea8871

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
