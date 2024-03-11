<script setup>
// Dummy data
let data = {
    tournaments: [
        {
            title: "CS2 - 5v5",
            desc: "Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet.",
            state: "OPEN",
            imageUrl: "https://i.ytimg.com/vi/aRRQuvD4E5E/maxresdefault.jpg",
            maxPlayerPerTeam: 3,
            gameID: 1,

        },
        {
            title: "CS2 - 2v2",
            desc: "Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet.",
            state: "OPEN",
            imageUrl: "https://i.ytimg.com/vi/aRRQuvD4E5E/maxresdefault.jpg",
            maxPlayerPerTeam: 3,
            gameID: 1,

        },
        {
            title: "CS2 - 1v1",
            desc: "Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet.",
            state: "OPEN",
            imageUrl: "https://i.ytimg.com/vi/aRRQuvD4E5E/maxresdefault.jpg",
            maxPlayerPerTeam: 3,
            gameID: 1,
        },
    ]
};
</script>

<template>
    <h1>Tournois</h1>
    <h2>Helloooo</h2>
    <p>{{ data["tournaments"][0]["title"] }}</p>
    <img :src="data['tournaments'][0]['imageUrl']">
</template>