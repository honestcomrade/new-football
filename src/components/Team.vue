<template>
    <div class="team-wrapper"  :style='{ backgroundImage: `url(${team.team.logoUrl})` }'>
      <div class="team-list">
        <ul>
          <li>
            <p class="header-item">{{team.team.teamLocation + " " + team.team.teamNickname}}</p>
          </li>
          <li>
            <p>Division Rank: {{team.team.record.divisionStanding}}</p>
          </li>
          <li>
            <p>This Week: {{team.score}}</p>
          </li>
          <li>
            <p>Total Score: {{team.team.record.pointsFor}}</p>
          </li>
        </ul>
      </div>
  </div>
</template>

<script>
export default {
  name: 'TeamComponent',
  data () {
    return {
    }
  },
  props: ['team']
}
</script>

<style>

.team-wrapper {
  border-radius: 2px;
  background-size: cover;
  background-position: center;
  width:auto;
  height: 250px;
  padding: 10px;
  margin:50px;
}

.header-item {
  color:rgb(244, 203, 66)
}

.team-list ul {
  margin: 40px 20px;

  border-radius: 4px;
  list-style:none;
  background-color:rgba(51, 51, 51, 0.8);
  padding: 8px 0;
  box-shadow:5px 10px 10px #333333;

}

.team-list ul li  {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-size:18px;
  display:block;
  height:24px;
  text-decoration:none;
  color:#bfe1f1;
  margin: 10px 5px;
  border-radius: 4px;

}

.team-list ul li :hover {
  -moz-transform:rotate(2deg);
  -moz-box-shadow:10px 10px 20px #000000;
  -webkit-transform:rotate(2deg);
  -webkit-box-shadow:10px 10px 20px #000000;
  transform:rotate(2deg);
  box-shadow:10px 10px 20px #000000;
  border-radius: 2px;
}

.team-list ul li p {
  margin: 10px;
  padding: 2px 10px;
 }

</style>
