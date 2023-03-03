# post_test1

quicksort

1. pertama yaitu mengimport library random agar array nntinya mempunyai angka-angka yang acak. Dan library os agar output terlihat bersih.
2. membuat fungsi quicksortnya, dengan parameter array, index pertama (0), dan index terakhir array (len(arr)).
3. jika array berisi <= 1 item, maka fungsi tidak akan dijalankan.
4. sebaliknya, fungsi rekursi akan dijalankan untuk mempartisi array menjadi beberapa bagian.
5. lalu di fungsi def partition, memiliki parameter yang sama dengan fungsi quicksort. Tujuannya untuk membandingkan item - item dalam sub array.
6. variabel left akan terus bertambah selama nilai lebih kecil dari pivot.
7. jika left bertemu dengan nilai yang lebih besar dari pivot, maka left akan berhenti.
8. selanjutnya variabel right akan berjalan untuk mencari nilai yang lebih kecil dari pivot. jika sudah ketemu, maka left tadi yang memegang nilai lebih besar
dari pivot akan ditukan nilainya dengan right yang memegang nilai lebih kecil dari pivot.
