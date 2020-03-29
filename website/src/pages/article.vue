<template>
	<div>
		<div class="top">
  			<div><img @click="tohead" src="../assets/logo2.png"/></div>
  				<div class="titles">
  					<span class="title" @click="totend">趋势指数</span>
  					<span class="title" @click="toexperience">股票体检</span>
  					<span class="title" @click="toknowledge">知识分享</span>
  					<span class="title" @click="tous">关于我们</span>
  					<span class="title" @click="toconsult">咨询</span>
  				</div>
  		</div>
  		<div class="middle">
  			<div class="title"><span>什么才是一个量化交易策略的核心？</span></div>
  			<div class="report">
  				<span class="author">环球时报</span>
  				<span class="author">19-12-11 22:00</span>
  			</div>
  			<div class="article">
  				
  			</div>
  		</div>
	</div>
</template>
<script>
	export default{
		name:'consult',
		data(){
			return{

			}
		},
		methods:{
			tohead(){
				this.$router.push('/')
			},
			tous(){
				this.$router.push('/us')
			},
      		toexperience(){
        		this.$router.push('/experience')
      		},
      		toconsult(){
        		this.$router.push('/consult')
      		},
      		toknowledge(){
      			this.$router.push('/knowledge')
      		},
      		totend(){
      			this.$router.push('/tend')
      		},
      		handleSelect(key, keyPath){
        		console.log(key,keyPath)
      		}
		}
	}
</script>
<style scoped lang="stylus">
.middle
	margin-top 100px
	text-align center
	.title
		color #c79288
		font-size 36px
	.report
		color #888888
		margin-top 30px
		font-size 16px
		.author
			margin 0 15px
.top
	margin-top 50px
	width 100%
	display flex
	justify-content space-between
	align-items center
	img
		height 40px
		width  160px
		margin-left 140px
		cursor pointer
	.titles
		margin-right 100px
		color #484848
		.title_i
			margin-right 20px
			cursor pointer
			padding-bottom 5px
			border-bottom 1px solid #484848
		.title 
			margin-right 20px
			cursor pointer
			padding-bottom 5px
		.title:hover
			border-bottom 1px solid #484848
</style>