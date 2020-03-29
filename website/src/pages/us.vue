<template>
	<div>
		<div class="top">
  			<div><img @click="tohead" src="../assets/logo2.png"/></div>
  				<div class="titles">
  					<span class="title" @click="totend">趋势指数</span>
  					<span class="title" @click="toexperience">股票体检</span>
  					<span class="title" @click="toknowledge">知识分享</span>
  					<span class="title_i">关于我们</span>
  					<span class="title" @click="toconsult">咨询</span>
  				</div>
  		</div>
		<div class="middle">
			<div class="text">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspAI趋势分析旨在传播机器学习技术在金融领域的应用，提供AI趋势指数，股票健康指数评估和量化知识分享，帮助您在智能时代通过机器算法实现低分险下的收益最大化。</div>
		</div>
		<div class="bottom">
			<div>
			<div class="contact">联系我们</div>
			<div class="contact">电话：13127667443</div>
			<div class="wechat">微信：xixichen06</div>
			</div>
		</div>
	</div>
</template>
<script>
	export default{
		name:'us',
		data(){
			return{
				activeIndex:'1'
			}
		},
		methods:{
			tohead(){
				this.$router.push('/')
			},
      		toexperience(){
        		this.$router.push('/experience')
      		},
      		toconsult(){
        		this.$router.push('/consult')
      		},
      		totend(){
      			this.$router.push('/tend')
      		},
      		handleSelect(key, keyPath){
        		console.log(key,keyPath)
			},
			toknowledge(){
        		this.$router.push('/knowledge')
      		},
		}
	}
</script>
<style scoped lang="stylus">
.top
	position absolute
	z-index 10
	top 50px
	left 0 
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
.middle
	margin-top 300px
	padding 0 150px
	.text
		font-size 26px
		color #c79288
		line-height 50px
.bottom
	margin-top 200px
	display flex
	justify-content center
	.contact
		text-align center
		margin-bottom 10px
	.wechat
		text-align center
		margin-top 10px
</style>