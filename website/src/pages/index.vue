<template>
  <div class="content">
  	<div class="banner">
  		<el-carousel :interval="4000" height="480px">
      		<el-carousel-item v-for="(item,index) in banners" :key="index">
        		<img :src="item.img" class="img"> 
      		</el-carousel-item>
    	</el-carousel>
  	</div>
  	<div class="top">
  		<div><img src="../assets/logo.png"/></div>
  		<div class="titles">
  			<span class="title" @click="totend">趋势指数</span>
  			<span class="title" @click="toexperience">股票体检</span>
  			<span class="title" @click="toknowledge">知识分享</span>
  			<span class="title" @click="tous">关于我们</span>
  			<span class="title" @click="toconsult">咨询</span>
  		</div>
  	</div>
  	<div class="middle">
  		<div class="slogen">使用深度学习的自动化交易系统</div>
  		<div class="try"><span class="text">尝试</span></div>
  	</div>
  	<div class="part">
  		<div class="title"><span>核心产品</span></div>
  		<div class="info" v-for="item in infos" @click="toarticle(item.id)"> 
  			<span class="s_title">{{item.title}}</span>
  			<div class="content">{{item.content}}</div>
  		</div>
  	</div>
  	<div class="bottom">
  		
  	</div>
  </div>  
</template>
<script>
	export default{
		name:'index',
		data(){
			return{
				banners:[{img:"https://image.linwushop.com/2020/01/16-20:14:55-/ae1091f7251df1742a82bbdb3b73b0cb.jpeg"},{img:"https://image.linwushop.com/2020/01/16-20:16:25-/f1f07e648977b5f5e213ab911c88f078.jpeg"},{img:"https://image.linwushop.com/2020/01/16-20:18:03-/7329abc1d396332d40ddad6e452fa1c3.jpeg"}
				],
				infos:[{
					title:"趋势指数",
					content:"通过深度学习的方法，我们不断更新股票投资组合列表并更新买入卖出的时间点和交易量，您可根据此指数购买相应股票",
					id:1
				},
				{
					title:"股票体检",
					content:"股票健康管理通过AI大数据分析的方式对您输入的股票进行健康体检，并给出投资建议",
					id:2
				},
				{
					title:"量化知识分享",
					content:"发布全新的AI量化技术的最新进展，定期举办技术沙龙帮你免费帮你解决量化交易过程中遇到的各种问题",
					id:3
				}]
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
      		toarticle(id){
      			this.$router.push({path:'/article',query:{id:id}})
      		}
		}
	}
</script>
<style scoped lang="stylus">
.banner
	img 
		width 100%
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
		color white
		.title_i
			margin-right 20px
			cursor pointer
			padding-bottom 5px
			border-bottom 1px solid #ffffff
		.title 
			margin-right 20px
			cursor pointer
			padding-bottom 5px
		.title:hover
			border-bottom 1px solid #ffffff
.middle
	z-index 10
	position absolute
	top 190px
	left 0 
	width 100%
	text-align center
	.slogen 
		color white
		font-size 45px
	.try
		margin-top 50px
		.text
			color #c79288
			border 1px solid #c79288
			padding 15px 40px
			cursor pointer
			font-size 20px
.part
	margin-top 70px
	text-align center
	.title
		color #c79288
		font-size 40px
	.info
		margin 70px 0 30px 0
		cursor pointer
		margin 0 140px
		padding 30px 0
		.s_title
			color #c79288
			font-size 30px
		.content
			color #666666
			font-size 18px
			margin 30px 0 10px 0
	.info:hover
		background-color #f1f1f1

	
</style>