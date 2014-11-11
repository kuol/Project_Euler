import scala.io.Source
 
//val a = Array.ofDim[Int](100, 50)

val N: Int = 10
// List of strings
val fileLines = Source.fromFile("numbers.txt").getLines.toList
// List of int arrays
val a = fileLines.map(line => line.take(N+2).toCharArray.map(_.asDigit))
val b = a.transpose.map(_.sum)


def digitize(x: Int) :List[Int] = {
  val h: Int = x/100
  val t: Int = (x - h*100)/10
  val o: Int = x%10
  List(h,t,o)
}


