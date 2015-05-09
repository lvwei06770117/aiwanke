package com.awanke.app.bean;

public class AppItem extends Entity {
	
	private int platformtype;//平台类型:android,ios
	private int appType;//应用类型:game,app
	private String appName;
	private String logoUrl;
	private String imageUrl;
	private String appDesc;
	private String downloadUrl;
	private int recommendUserId;
	private String recommendation;
	private int loveNum;
	private int playedNum;
	private int downloadedNum;
	private int commentCount;
	private String createDate;
	
	public int getPlatformtype() {
		return platformtype;
	}
	public void setPlatformtype(int platformtype) {
		this.platformtype = platformtype;
	}
	public int getAppType() {
		return appType;
	}
	public void setAppType(int appType) {
		this.appType = appType;
	}
	public String getLogoUrl() {
		return logoUrl;
	}
	public void setLogoUrl(String logoUrl) {
		this.logoUrl = logoUrl;
	}
	public String getAppName() {
		return appName;
	}
	public void setAppName(String appName) {
		this.appName = appName;
	}
	public String getAppDesc() {
		return appDesc;
	}
	public void setAppDesc(String appDesc) {
		this.appDesc = appDesc;
	}
	public String getImageUrl() {
		return imageUrl;
	}
	public void setImageUrl(String imageUrl) {
		this.imageUrl = imageUrl;
	}
	public String getDownloadUrl() {
		return downloadUrl;
	}
	public void setDownloadUrl(String downloadUrl) {
		this.downloadUrl = downloadUrl;
	}
	public String getRecommendation() {
		return recommendation;
	}
	public void setRecommendation(String recommendation) {
		this.recommendation = recommendation;
	}
	public int getRecommendUserId() {
		return recommendUserId;
	}
	public void setRecommendUserId(int recommendUserId) {
		this.recommendUserId = recommendUserId;
	}
	public int getLoveNum() {
		return loveNum;
	}
	public void setLoveNum(int loveNum) {
		this.loveNum = loveNum;
	}
	public int getPlayedNum() {
		return playedNum;
	}
	public void setPlayedNum(int playedNum) {
		this.playedNum = playedNum;
	}
	public int getDownloadedNum() {
		return downloadedNum;
	}
	public void setDownloadedNum(int downloadedNum) {
		this.downloadedNum = downloadedNum;
	}
	public int getCommentCount() {
		return commentCount;
	}
	public void setCommentCount(int commentCount) {
		this.commentCount = commentCount;
	}
	public String getCreateDate() {
		return createDate;
	}
	public void setCreateDate(String createDate) {
		this.createDate = createDate;
	}
	
	
	
	

}
