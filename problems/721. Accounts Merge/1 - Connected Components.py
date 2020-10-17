from typing import List, Set


class Graph:
    def __init__(self, v: int):
        self.__adj = [set() for _ in range(v)]
        self.__v = v

    def add_edge(self, v: int, w: int):
        self.__adj[v].add(w)
        self.__adj[w].add(v)

    def adj(self, v: int) -> Set[int]:
        return self.__adj[v]

    def v(self) -> int:
        return self.__v


class SymbolGraph:
    def __init__(self, accounts: List[List[str]]):
        self.__st = st = {}
        for [_, *account_emails] in accounts:
            for email in account_emails:
                st.setdefault(email, len(st))

        self.__keys = keys = list(st.keys())
        self.__graph = graph = Graph(len(keys))
        for i, [_, first_email, *other_emails] in enumerate(accounts):
            for email in other_emails:
                graph.add_edge(st[first_email], st[email])

    def index(self, key: str) -> int:
        return self.__st[key]

    def name(self, v: int) -> str:
        return self.__keys[v]

    def graph(self) -> Graph:
        return self.__graph


class ConnectedComponents:
    def __init__(self, graph: Graph):
        self.__marked = [False] * graph.v()
        self.__id = [0] * graph.v()
        self.__count = 0

        for i in range(graph.v()):
            if not self.__marked[i]:
                self.__dfs(graph, i)
                self.__count += 1

    def __dfs(self, graph: Graph, v: int):
        self.__marked[v] = True
        self.__id[v] = self.__count
        for w in graph.adj(v):
            if not self.__marked[w]:
                self.__dfs(graph, w)

    def count(self):
        return self.__count

    def id(self, v: int):
        return self.__id[v]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        symbol_graph = SymbolGraph(accounts)
        graph = symbol_graph.graph()
        cc = ConnectedComponents(graph)

        result = [[] for _ in range(cc.count())]
        for i in range(graph.v()):
            result[cc.id(i)].append(symbol_graph.name(i))

        for j in range(cc.count()):
            result[j].sort()

        email_account = self.__email_account(accounts)
        for k in range(cc.count()):
            email = result[k][0]
            account_id = email_account[email]
            result[k].insert(0, accounts[account_id][0])

        return result

    def __email_account(self, accounts: List[List[str]]):
        email_owners = {}
        for i, [_, *account_emails] in enumerate(accounts):
            for email in account_emails:
                email_owners.setdefault(email, i)
        return email_owners
