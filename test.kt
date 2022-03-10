fun add(n1: Int, n2: Int):String = (n1 + n2).toString();

fun add_print(n1: Int, n2: Int):Unit {
    println("sum of $n1 and $n2 is ${n1 + n2}");
}

fun main(args: Array<String>) {
    println(add(args[0].toInt(), args[1].toInt()));
    add_print(args[0].toInt(), args[1].toInt());
}
