# 🔤 Lexicographically Smallest Equivalent String

🔗 **Problem Link:** [Lexicographically Smallest Equivalent String →](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/)

## 📝 Description

You are given two strings `s1` and `s2` of the same length, and a string `baseStr`.

We say that two characters `x` and `y` are **equivalent** if any of the following are true:

- `x == y`
- `x` is equivalent to `y`
- `y` is equivalent to `x`
- `x` is equivalent to `z` and `z` is equivalent to `y` for some character `z`

For example, if `s1 = "abc"` and `s2 = "cde"`, then the equivalences are: `'a' ~ 'c'`, `'b' ~ 'd'`, `'c' ~ 'e'`.

Using these equivalences, you can **replace** any character in `baseStr` with any of its equivalent characters to form a new string.

Return the **lexicographically smallest** equivalent string possible after applying the equivalency rules.

---

## 💡 Example

```txt
Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"

Explanation:
Equivalences: p~m, a~o, r~r, k~i, e~s
"parser" becomes "makkek", which is the lex smallest form.
```

---

## 📚 Constraints

- `1 <= s1.length, s2.length, baseStr.length <= 1000`
- `s1.length == s2.length`
- `s1`, `s2`, and `baseStr` consist of lowercase English letters.

---

## 📌 Tags

- [String →](https://leetcode.com/problem-list/strings/)
- [Union Find →](https://leetcode.com/tag/union-find/)
- [Graph →](https://leetcode.com/problem-list/graph/)