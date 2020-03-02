open System

let WORD = "hackerrank"

let rec GetHackerRank wordToTest word =
    if String.length wordToTest < 1 or String.length word < 1
    then
        if String.length word < 1 then
            printf "YES\n" 
        else
            printf "NO\n"
    else
        let newWord = if wordToTest.[0] = word.[0] then word.[1..] else word
        GetHackerRank wordToTest.[1..] newWord

let rec ExecuteAllWords words =
    match words with 
    | head :: tail -> 
        GetHackerRank head WORD
        ExecuteAllWords tail
    | [] -> ()

let _, N = Console.ReadLine() |> Int32.TryParse
let words = [for _ in 1..N -> Console.ReadLine()]

ExecuteAllWords words |> ignore
