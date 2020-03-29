<template>
	<div>
		<div class="top">
  			<div><img @click="tohead" src="../assets/logo2.png"/></div>
  				<div class="titles">
  					<span class="title" @click="totend">趋势指数</span>
  					<span class="title_i">股票体检</span>
  					<span class="title" @click="toknowledge">知识分享</span>
  					<span class="title" @click="tous">关于我们</span>
  					<span class="title" @click="toconsult">咨询</span>
  				</div>
  		</div>
		<div class="middle">
			<div class="default">
				<el-input style="width:500px" placeholder="输入股票代码或名称，如000325 久之洋" />
				<img src="../assets/search.png" />
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
		name:'service',
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
      		toknowledge(){
        		this.$router.push('/knowledge')
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
	margin-top 300px
	.default
		display flex
		justify-content center
		img 
			width 40px
			height  40px
			margin-left 20px
			cursor pointer
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