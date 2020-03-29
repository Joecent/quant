<template>
	<div>
		<div class="top">
  			<div><img @click="tohead" src="../assets/logo2.png"></div>
  				<div class="titles">
  					<span class="title_i">趋势指数</span>
  					<span class="title" @click="toexperience">股票体检</span>
  					<span class="title" @click="toknowledge">知识分享</span>
  					<span class="title" @click="tous">关于我们</span>
  					<span class="title" @click="toconsult">咨询</span>
  				</div>
  		</div>
		<div class="middle">
			<div class="point">
				<div class="title">趋势指数：3189点</div>
				<div class="tips">近3月累计涨幅：30%</div>
				<div class="tips">近6月累计涨幅：87%</div>
				<div class="tips">近1年累计涨幅：132%</div>
			</div>
			<div class="bags">
				<div class="title">趋势指数基础包</div>
				<div class="tips">600242.SH 中昌数据</div>
				<div class="tips">300395.SZ 菲利华</div>
				<div class="tips">300298.SZ 三诺生物</div>
				<div class="tips">000998.SZ 隆平高科</div>
			</div>
			<div class="record">
				<div class="title">交易记录</div>
				<div class="tips">2020.1.10买入200手600242.SH 中昌数据</div>
				<div class="tips">2020.1.10卖出100手300395.SZ 菲利华</div>
				<div class="tips">2020.1.13卖出100手300395.SZ 菲利华</div>
				<div class="tips">2020.1.19卖出100手300395.SZ 菲利华</div>
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
		name:'tend',
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
      		toknowledge(){
      			this.$router.push('/knowledge')
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
	display flex
	justify-content space-between
	padding 0 120px 0 150px
	margin-top 250px
	.title
		font-size 29px
		margin-bottom 30px
	.tips
		font-size 22px
		color  #444444
		margin 10px 0
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