links = response.xpath(
    '//div[@class="m-con"]//a/@href|//div[@id="productlist"]//a/@href|//ul[@class="channel-newsGroup"]/li/a/@href|//div[@class="m-con m-box7"]//a/@href|//div[@class="m-list6"]//ul//a/@href').extract()
