const axios = require('axios')

function getMapData() {
    return axios({  
        url: 'https://gps.hackmirror.icu/api/map',
        method: 'get',
        params: {
            user: 'xwinxu_be206c',
        }
    })
}

function reset() {
    return axios({  
        url: 'https://gps.hackmirror.icu/api/reset',
        method: 'post',
        params: {
            user: 'xwinxu_be206c',
        }
    })
}

function bfs(adjList, start, end) {
    let queue = [start]
    let parent = {}
    parent[start] = null

    i = 1
    while(queue.length) {
        let next = []
        queue.forEach(function(u) {
            adjList[u].forEach(function(v) {
                if(!parent.hasOwnProperty(v)){
                    parent[v] = u
                    next.push(v)
                }
            })
        })
        i++
        queue = next

        if(parent.hasOwnProperty(end)){
            return parent
        }
    }
    return null
}

function getPath(tree, end){
    nodes = [end]
    nextNode = tree[end]

    while(nextNode !== null) {
        nodes.push(nextNode)
        nextNode = tree[nodes[nodes.length-1]]
    }

    return nodes.reverse()
}

function getMove(path) {
    moves = {
        '1': 'right',
        '-1': 'left',
        '150': 'down',
        '-150': 'up'
    }

    return Promise.resolve(moves[path[1]-path[0]])
}

function makeMove(newMove) {
    return axios({  
        url: 'https://gps.hackmirror.icu/api/move',
        method: 'post',
        params: {
            user: 'xwinxu_be206c',
            move: newMove
        }
    })
}

function fuck(pos) {
    return getMapData()
    .then(response => {
        return response.data.graph
    })
    .then(adjList => {
        return bfs(adjList, pos, 22499)
    })
    .then(tree => {
        return getPath(tree, 22499)
    })
    .then(path => {
        if(!path) {
            return reject('lol')
        }
        if(path.length < 3) {
            process.exit()
        }

        return getMove(path)
    })
    .then(move => {
        return makeMove(move)
    })
}

function main(pos) {
    fuck(pos)
    .then(response => {
        console.log(pos)
        setTimeout(() => {
            main(response.data.row*150 + response.data.col)
        }, 50);
    })
    .catch(err => {
        reset()
        main(0)
    })
}

main(0)
