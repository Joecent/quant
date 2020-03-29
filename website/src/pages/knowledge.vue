<template>
	<div>
		<div class="top">
  			<div><img @click="tohead" src="../assets/logo2.png"/></div>
  				<div class="titles">
  					<span class="title" @click="totend">趋势指数</span>
  					<span class="title" @click="toexperience">股票体检</span>
  					<span class="title_i">知识分享</span>
  					<span class="title" @click="tous">关于我们</span>
  					<span class="title" @click="toconsult">咨询</span>
  				</div>
  		</div>
		<div class="middle">
			<div class="topic">
				<div class="time">12/2/19</div>
				<div class="title">什么是量化交易</div>
				<div class="content">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp量化交易是指以先进的数学模型替代人为的主观判断，利用计算机技术从庞大的历史数据中海选能带来超额收益的多种“大概率”事件以制定策略。</div>
				<div class="more">more&nbsp&nbsp>></div>
			</div>
			<div class="topic">
				<div class="time">12/2/19</div>
				<div class="title">什么是量化交易</div>
				<div class="content">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp量化交易是指以先进的数学模型替代人为的主观判断，利用计算机技术从庞大的历史数据中海选能带来超额收益的多种“大概率”事件以制定策略。</div>
				<div class="more">more&nbsp&nbsp>></div>
			</div>
			<div class="topic">
				<div class="time">12/2/19</div>
				<div class="title">什么是量化交易</div>
				<div class="content">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp量化交易是指以先进的数学模型替代人为的主观判断，利用计算机技术从庞大的历史数据中海选能带来超额收益的多种“大概率”事件以制定策略。</div>
				<div class="more">more&nbsp&nbsp>></div>
			</div>
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
		name:'knowledge',
		data(){
			return{
				activeIndex:'1'
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
	margin-top 200px
	padding 0 40px
	display flex
	.topic
		padding 30px 50px
		cursor pointer
		.time
			text-align center
			color #333333
		.title
			text-align center
			margin 20px 0 30px 0
			font-size 26px
			color #c79288
		.content
			text-align center
			line-height 30px
			color #333333
		.more
			text-align center
			margin-top 10px
			color #c79288
			font-size 14px
	.topic:hover
		background-color #f1f1f1
.bottom
	margin-top 100px
	display flex
	justify-content center
	.contact
		text-align center
		margin-bottom 10px
	.wechat
		text-align center
		margin-top 10px
</style>