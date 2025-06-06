class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def parse_baseStr(baseStr) -> list[str]:
            return list(baseStr)

        def make_annotations(s1: str, s2: str) -> list[list[str]]:
            groups: list[set[str]] = [set(pair) for pair in zip(s1, s2)]

            changed = True

            while changed:
                changed = False
                i = 0
                while i < len(groups):
                    j = i + 1
                    while j < len(groups):
                        if groups[i] & groups[j]:
                            groups[i] |= groups[j]
                            groups.pop(j)
                            changed = True
                        else:
                            j += 1
                    i += 1

            return [sorted(g) for g in groups]

        annotations = make_annotations(s1, s2)

        rep = {ch: g[0] for g in annotations for ch in g}

        return ''.join(rep.get(ch, ch) for ch in baseStr)