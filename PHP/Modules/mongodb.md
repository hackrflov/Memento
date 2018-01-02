```bash
$ pecl install mongodb
$ vim /etc/php.ini
# Add following setting
extension=mongodb.so
$ cd yourprojectroot
$ composer require mongodb/mongodb
$ vim index.php
```
```php
<?php
// This path should point to Composer's autoloader
require 'vendor/autoload.php';

$client = new MongoDB\Client("mongodb://localhost:27017");
$collection = $client->demo->beers;

$result = $collection->find( [ 'name' => 'Hinterland', 'brewery' => 'BrewDog' ] );

foreach ($result as $entry) {
    echo $entry['_id'], ': ', $entry['name'], "\n";
}

// To find with filter and sort
$filter = array($key => $value);
$sort = array($field1 => -1, $field2 => 1);
$options = array('sort' => $sort);
$collection->find($filter, $options);

// count
$collection->count($filter);
```
