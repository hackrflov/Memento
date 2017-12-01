
- `json_decode($string, $assoc)`: convert string to json, if $assoc is true, returned object will be array
- `json_encode($string)`: convert json to string
- `str_replace($search, $replace, $subject)`: replace substring
- `substr($string, $start, $end)`: return substring
- `is_string($var)`: test whether a value is string


Common Bugs
-----------
1. Json object cannot be 'echo', we must use `var_dump(json)`
