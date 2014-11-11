def sumOfSquare(n: Int): Long = {
  if (n==1) 1
  else n*n + sumOfSquare(n-1)
}

def sum(n: Int): Long = {
  if (n==1) 1 else n + sum(n-1)
}

val temp = sum(100)
val result = temp*temp - sumOfSquare(100)
//println(s"Result: $result \n")
println("Result: "+ result + "\n")
