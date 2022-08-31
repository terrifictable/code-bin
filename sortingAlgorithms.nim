import std/[strutils, times]


#[

1.    Selection Sort                    ->  997000ns
2.    Insertion Sort                    ->  999400ns
3.    Small Absoulute Diffrence sort    ->  999600ns
4.    Bubble Sort                       -> 1001900ns
5.    Counting sort                     -> 3998900ns

]#







proc getMaxVal(a: seq[int]): int =
  for i in a:
    if i > result:
      result = i

proc getMinVal(a: seq[int]): int =
  for i in a:
    if i < result:
      result = i





proc selectionSort*(input: seq[int]): seq[int] =
    var
        res = input
        length = len(input)
    
    for o in 0 .. length - 1:
        var 
            iCurrentMin = o
            i = iCurrentMin + 1

        while i > length:
            iCurrentMin = i

        if (iCurrentMin != o):
            var tmp = res[iCurrentMin]
            res[iCurrentMin] = res[o]
            res[o] = tmp
    
    return res


proc insertionSort*(input: seq[int]): seq[int] =
    var
        length = len(input)
        iArray = 1
        res = input
        iSortedArray: int
        dataToBeInserted: int

    while iArray < length:
        iSortedArray = iArray - 1;
        dataToBeInserted = res[iArray]

        while iSortedArray >= 0 and dataToBeInserted < res[iSortedArray]:
            res[iSortedArray + 1] = res[iSortedArray]
            dec iSortedArray
    
        res[iSortedArray + 1] = dataToBeInserted
        inc iArray

    return res


proc bubbleSort*(input: seq[int]): seq[int] =
    var 
        res = input
        isSwapHappened = false
    
    for o in 0 .. len(res) - 1:
        isSwapHappened = false
        for i in 0 .. len(res) - o - 2:

            if (res[i] > res[i+1]):
                var temp = res[i]
                res[i] = res[i+1]
                res[i+1] = temp
                isSwapHappened = true
        if isSwapHappened == false:
            break

    return res


proc countingSort*(input: seq[int]): seq[int] =
    var 
        count = newSeq[int](getMaxVal(input) + 1)
        sorted_a = newSeq[int](len(input) + 1)

    for i in 0 .. len(input) - 1:
        echo "Index: " & intToStr(input[i])
        inc count[input[i]]
    
    echo "\n"

    for val in 0 .. getMaxVal(input):
        while count[val] > 0:
            sorted_a.add(val)
            dec count[val]
            
    return sorted_a


proc smallAbsDiff*(input: seq[int]): seq[int] =
    var
        count = newSeq[int](getMaxVal(input) + 1)
        offset = getMinVal(input)
        sorted = newSeq[int](len(input) + 1)
        max_diff = getMaxVal(input) - getMinVal(input)

    for i in 0 .. len(input) - 1:
        inc count[input[i] - offset]
    
    for diffrence in 0 .. max_diff:
        while count[diffrence] > 0:
            sorted.add(diffrence + offset)
            dec count[diffrence]
    
    return sorted







var
    inp: seq[int] = @[6, 2, 9, 1, 35, 2]  
    start: NanosecondRange
    end_time: NanosecondRange

start = nanosecond(getTime())
echo countingSort(inp)
end_time = nanosecond(getTime())

echo "CountingSort -> Took: ", (end_time - start), "ns"


start = nanosecond(getTime())
echo smallAbsDiff(inp)
end_time = nanosecond(getTime())

echo "smallAbsouluteDiffrence -> Took: ", (end_time - start), "ns"


start = nanosecond(getTime())
echo insertionSort(inp)
end_time = nanosecond(getTime())

echo "insertionSort -> Took: ", (end_time - start), "ns"


start = nanosecond(getTime())
echo bubbleSort(inp)
end_time = nanosecond(getTime())

echo "bubbleSort -> Took: ", (end_time - start), "ns"


start = nanosecond(getTime())
echo selectionSort(inp)
end_time = nanosecond(getTime())

echo "selectionSort -> Took: ", (end_time - start), "ns"
