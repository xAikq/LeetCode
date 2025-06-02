# ⚾ Baseball Game

🔗 **Problem Link:** [Baseball Game →](https://leetcode.com/problems/baseball-game/description/)

## 📝 Description

You are keeping score for a baseball game with strange rules. The game consists of several operations represented by a list of strings `operations`, where each operation is one of the following:

- An **integer** `x` — Record a new score of `x`.
- `"+"` — Record a new score that is the **sum of the previous two scores**.
- `"D"` — Record a new score that is **double the previous score**.
- `"C"` — Invalidate the **previous score**, removing it from the record.

Return the **sum of all the scores** after performing all the operations.

It is guaranteed that every operation is valid. The list always has at least one element, and the operations will always result in a valid record.

---

## 💡 Example

```txt
Input: operations = ["5", "2", "C", "D", "+"]
Output: 30

Explanation:
"5" → record [5]
"2" → record [5, 2]
"C" → remove 2 → [5]
"D" → record 10 (2×5) → [5, 10]
"+" → record 15 (5+10) → [5, 10, 15]
Sum = 5 + 10 + 15 = 30
```

---

## 📚 Constraints

- `1 <= operations.length <= 1000`
- `operations[i]` is `"C"`, `"D"`, `"+"`, or a string representing an integer in the range `[-3 * 10⁴, 3 * 10⁴]`
- The answer will always fit in a 32-bit integer.

---

## 📌 Tags

- [Array →](https://leetcode.com/problem-list/array/)
- [Stack →](https://leetcode.com/problem-list/stack/)
- [Simulation →](https://leetcode.com/problem-list/simulation/)