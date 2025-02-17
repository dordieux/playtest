# レスポンスのJSONの小数値をアサートできる

## JSON Path
* レスポンスボディとしてシナリオデータストアに"{ \"key1\": 10.00, \"key2\": [ 0.01 ] }"を保存する
* レスポンスのJSONの"$.key1"が小数の"10.00"である
* レスポンスのJSONの"$.key2[0]"が小数の"0.01"である

## JSON Pathで指定したオブジェクトが一致しない
* レスポンスボディとしてシナリオデータストアに"{ \"key1\": 10.00, \"key2\": [ 0.01 ] }"を保存する
* レスポンスのJSONの"$.key1"が小数の"0.01"でない
* レスポンスのJSONの"$.key2[0]"が小数の"10.00"でない

## JSON Pathで指定した配列を条件で絞った1要素
* レスポンスボディとしてシナリオデータストアに"{\"key1\":[{\"id\":\"a\",\"key3\":1.0}, {\"id\":\"b\",\"key3\": 2.0 }, {\"id\":\"c\",\"key3\":3.0}]}"を保存する
* レスポンスのJSONの"$.key1"の配列の、UniqueKey"id"の値が"b"である要素の"key3"が、小数値の"2.0"である

## 配列内における存在（有）
* レスポンスボディとしてシナリオデータストアに"{\"tests\": [1.1, 2.1, 3.1]}"を保存する
* レスポンスのJSONの配列"$.tests"に、小数値"3.1"が存在する

## 配列内において存在（無）
* レスポンスボディとしてシナリオデータストアに"{\"tests\": [1.0, 3.3]}"を保存する
* レスポンスのJSONの配列"$.tests"に、小数値"2.1"が存在しない
